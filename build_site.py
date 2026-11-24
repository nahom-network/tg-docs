"""Assemble a GitHub Pages artifact. Preview: python -m http.server -d _site 8000."""

import argparse
import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
from urllib.parse import urlsplit

import build_llms


SERVERLESS_SOURCE = Path("serverless-docs.md")


def normalize_site_url(site_url):
    if not site_url:
        return None
    parts = urlsplit(site_url)
    if (parts.scheme not in ("https", "http") or not parts.netloc
            or parts.query or parts.fragment or parts.username or parts.password
            or any(character.isspace() for character in site_url)):
        raise ValueError(
            "Site URL must be an absolute HTTP(S) homepage URL without credentials, query, or fragment"
        )
    return site_url.rstrip("/") + "/"


def section_description(section):
    description = next((line.strip() for line in section.lines
                        if line.strip() and not line.startswith(("#", "|", ">", "-", "```", "~~~"))), "")
    description = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", description)
    description = re.sub(r"[*`_]", "", description)
    return description[:220]


def load_document(text, externals=None):
    files = build_llms.build(text, externals)
    title, url, summary, sections = build_llms.parse_document(text)
    date = re.search(r'^date:\s*["\']?([^"\'\n]+)', text, re.M)
    version = re.search(r"\*\*Bot API ([\d.]+)\*\*", text)
    catalog = {
        "title": title,
        "source": url,
        "summary": summary,
        "updated_at": date[1].strip() if date else None,
        "version": version[1] if version else None,
        "page_count": len(sections),
        "sections": [],
    }
    for section in sections:
        catalog["sections"].append({
            "title": section.title,
            "group": section.group,
            "path": section.path,
            "description": section_description(section),
        })
    return files, catalog


def render_catalog(catalog):
    groups = {}
    for section in catalog["sections"]:
        groups.setdefault(section["group"], []).append(section)
    rendered = []
    for group, entries in groups.items():
        links = []
        for entry in entries:
            links.append(
                f'<a class="section-link" href="{escape(entry["path"], quote=True)}">'
                f'<span><span class="section-name">{escape(entry["title"])}</span>'
                f'<span class="section-description">{escape(entry["description"])}</span></span>'
                '<span class="section-arrow" aria-hidden="true">↗</span></a>')
        rendered.append(f'<section class="group-block"><h3 class="group-title">{escape(group)}</h3>'
                        f'<div class="group-links">{"".join(links)}</div></section>')
    return "\n".join(rendered)


def render_page(template, catalog, page_url, name, description):
    html = template.read_text(encoding="utf-8")
    # Render the same catalog in HTML so discovery never depends on JavaScript.
    html = re.sub(r"<!-- CATALOG_START -->.*?<!-- CATALOG_END -->",
                  lambda _: render_catalog(catalog), html, flags=re.S)
    count = catalog["page_count"]
    html = html.replace(
        'aria-live="polite">Loading section catalog…</span>',
        f'aria-live="polite">{count} pages in the mirror</span>')
    html = html.replace(
        '<p id="search-summary" class="search-summary" aria-live="polite"></p>',
        f'<p id="search-summary" class="search-summary" aria-live="polite">{count} sections</p>')
    schema = {"@context": "https://schema.org", "@type": "WebPage",
              "name": name, "description": description, "inLanguage": "en",
              "isBasedOn": catalog["source"]}
    url_metadata = ""
    if page_url:
        schema["url"] = page_url
        url_metadata = (f'<link rel="canonical" href="{escape(page_url, quote=True)}">\n'
                        f'  <meta property="og:url" content="{escape(page_url, quote=True)}">')
    schema_json = json.dumps(schema, ensure_ascii=False).replace("<", "\\u003c")
    return html.replace(
        "<!-- SEO_URL_METADATA -->",
        url_metadata + f'\n  <script type="application/ld+json">{schema_json}</script>')


def build_site(api_source, output, site_url=None, serverless_source=SERVERLESS_SOURCE,
               externals=None):
    site_url = normalize_site_url(site_url)
    api_text = api_source.read_text(encoding="utf-8-sig")
    api_files, api_catalog = load_document(api_text, externals)
    serverless_text = serverless_source.read_text(encoding="utf-8-sig")
    serverless_files, serverless_catalog = load_document(serverless_text, externals)

    files = dict(api_files)
    for name, content in serverless_files.items():
        files[f"serverless/{name}"] = content
    files["docs.json"] = json.dumps(api_catalog, ensure_ascii=False, indent=2) + "\n"
    files["serverless/docs.json"] = json.dumps(serverless_catalog, ensure_ascii=False, indent=2) + "\n"
    files[".nojekyll"] = ""

    root = Path(__file__).resolve().parent
    files["index.html"] = render_page(
        root / "templates" / "index.html", api_catalog, site_url,
        "Telegram Bot API Docs for LLMs",
        "An independent Telegram Bot API reference with llms.txt and linked Markdown documentation.")
    serverless_url = site_url + "serverless/" if site_url else None
    files["serverless/index.html"] = render_page(
        root / "templates" / "serverless.html", serverless_catalog, serverless_url,
        "Telegram Serverless Docs for LLMs",
        "An independent Telegram Serverless reference with llms.txt and linked Markdown documentation.")
    # Keep the old extension-based address working after the landing page moved
    # to the serverless/ directory.
    files["serverless.html"] = (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '  <meta charset="utf-8">\n'
        '  <meta http-equiv="refresh" content="0; url=serverless/">\n'
        '  <link rel="canonical" href="serverless/">\n'
        '  <title>Telegram Serverless Docs for LLMs</title>\n'
        '</head>\n<body><p>Redirecting to '
        '<a href="serverless/">the Serverless reference</a>.</p></body>\n</html>\n')
    # A branch-based Pages deployment ignores the custom-domain setting's CNAME
    # unless the file is part of the published tree.
    cname = root / "CNAME"
    if cname.is_file():
        files["CNAME"] = cname.read_text(encoding="utf-8").strip() + "\n"

    if site_url:
        urls = [site_url, serverless_url]
        files["sitemap.xml"] = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{escape(url)}</loc></url>\n" for url in urls)
            + "</urlset>\n")
    files["robots.txt"] = "User-agent: *\nAllow: /\n" + (
        f"\nSitemap: {site_url}sitemap.xml\n" if site_url else "")

    payloads = {name: content.encode("utf-8") for name, content in files.items()}
    for path in (root / "assets").rglob("*"):
        if path.is_file():
            payloads[path.relative_to(root).as_posix()] = path.read_bytes()
    # Retire only tracked build outputs, never arbitrary files in the directory.
    manifest_path = output / ".site-manifest.json"
    previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    retired = []
    for name, digest in previous.items():
        if name in payloads:
            continue
        path = output / name
        if not path.resolve().is_relative_to(output.resolve()):
            raise ValueError("Invalid path in site build manifest")
        if path.is_file():
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise ValueError(f"Obsolete output was modified; move it before rebuilding: {path}")
            retired.append(path)
    output.mkdir(parents=True, exist_ok=True)
    for path in retired:
        path.unlink()
    for name, content in payloads.items():
        path = output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    manifest_path.write_text(json.dumps({name: hashlib.sha256(content).hexdigest()
                                        for name, content in payloads.items()}, indent=2) + "\n")
    print(f"Site ready in {output}: {api_catalog['page_count']} API pages, "
          f"{serverless_catalog['page_count']} Serverless pages")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("tg-docs.md"))
    parser.add_argument("--serverless-input", type=Path, default=SERVERLESS_SOURCE)
    parser.add_argument("--externals", type=Path, default=Path("external-docs"),
                        help="Mirrored Telegram pages saved by update_docs.py (default: external-docs)")
    parser.add_argument("--output", type=Path, default=Path("_site"))
    parser.add_argument("--site-url", default=os.environ.get("SITE_URL"),
                        help="Public homepage URL, including repository subpath; defaults to SITE_URL")
    args = parser.parse_args()
    build_site(args.input, args.output, args.site_url, args.serverless_input,
               build_llms.load_externals(args.externals))
