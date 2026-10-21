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


def build_site(source, output, site_url=None):
    if site_url:
        parts = urlsplit(site_url)
        if (parts.scheme not in ("https", "http") or not parts.netloc
                or parts.query or parts.fragment or parts.username or parts.password
                or any(character.isspace() for character in site_url)):
            raise ValueError("Site URL must be an absolute HTTP(S) homepage URL without credentials, query, or fragment")
        site_url = site_url.rstrip("/") + "/"
    text = source.read_text(encoding="utf-8-sig")
    files = build_llms.build(text)
    title, url, sections = build_llms.parse_document(text)
    date = re.search(r'^date:\s*["\']?([^"\'\n]+)', text, re.M)
    version = re.search(r"\*\*Bot API ([\d.]+)\*\*", text)
    catalog = {
        "title": title,
        "source": url,
        "updated_at": date[1].strip() if date else None,
        "version": version[1] if version else None,
        "page_count": len(sections),
        "sections": [],
    }
    for section in sections:
        description = next((line.strip() for line in section.lines
                            if line.strip() and not line.startswith(("#", "|", ">", "-", "```", "~~~"))), "")
        description = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", description)
        description = re.sub(r"[*`_]", "", description)
        catalog["sections"].append({"title": section.title, "group": section.group,
                                    "path": section.path, "description": description[:220]})
    files["docs.json"] = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    files[".nojekyll"] = ""
    root = Path(__file__).resolve().parent
    html = (root / "index.html").read_text(encoding="utf-8")
    # Render the same catalog in HTML so discovery never depends on JavaScript.
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
    html = re.sub(r"<!-- CATALOG_START -->.*?<!-- CATALOG_END -->",
                  lambda _: "\n".join(rendered), html, flags=re.S)
    schema = {"@context": "https://schema.org", "@type": "WebPage",
              "name": "Telegram Bot API Docs for LLMs",
              "description": "An independent Telegram Bot API reference with llms.txt and linked Markdown documentation.",
              "inLanguage": "en", "isBasedOn": url}
    url_metadata = ""
    if site_url:
        schema["url"] = site_url
        url_metadata = (f'<link rel="canonical" href="{escape(site_url, quote=True)}">\n'
                        f'  <meta property="og:url" content="{escape(site_url, quote=True)}">')
        files["sitemap.xml"] = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                f'  <url><loc>{escape(site_url)}</loc></url>\n</urlset>\n')
    files["robots.txt"] = "User-agent: *\nAllow: /\n" + (f"\nSitemap: {site_url}sitemap.xml\n" if site_url else "")
    schema_json = json.dumps(schema, ensure_ascii=False).replace("<", "\\u003c")
    html = html.replace("<!-- SEO_URL_METADATA -->",
                        url_metadata + f'\n  <script type="application/ld+json">{schema_json}</script>')
    files["index.html"] = html
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
    print(f"Site ready in {output}: {len(sections)} API pages")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("tg-docs.md"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    parser.add_argument("--site-url", default=os.environ.get("SITE_URL"),
                        help="Public homepage URL, including repository subpath; defaults to SITE_URL")
    args = parser.parse_args()
    build_site(args.input, args.output, args.site_url)
