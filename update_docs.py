"""Fetch the official documentation, convert it, then rebuild LLM files."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import time
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

import build_llms


API_URL = "https://core.telegram.org/bots/api"
SERVERLESS_URL = "https://core.telegram.org/bots/serverless"
SERVERLESS_MARKDOWN_URL = "https://core.telegram.org/bots/serverless.md"
SERVERLESS_SUMMARY = (
    "Run backend code for your bot and Mini App directly on Telegram's infrastructure."
)
API_INPUT = Path("tg-docs.md")
API_OUTPUT = Path(".")
SERVERLESS_INPUT = Path("serverless-docs.md")
SERVERLESS_OUTPUT = Path("serverless")
EXTERNAL_DIR = Path("external-docs")


class APIConverter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags):
        # Telegram's Markdown examples contain triple-backtick fences themselves.
        # An outer fence must be longer or the splitter sees example headings.
        code = el.find("code")
        classes = code.get("class", []) if code else []
        language = next((value[9:] for value in classes if value.startswith("language-")), "")
        raw = el.get_text().strip("\n")
        longest = max((len(run) for run in re.findall(r"`+", raw)), default=0)
        fence = "`" * max(3, longest + 1)
        return f"\n\n{fence}{language}\n{raw}\n{fence}\n\n"


def convert_html(html, source=API_URL):
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("#dev_page_content")
    if content is None:
        raise ValueError("Official page no longer contains #dev_page_content")
    for node in content.select("script, style, .anchor"):
        node.decompose()
    # Resolve links before conversion; code examples are text, not HTML nodes.
    for node in content.select("[href], [src]"):
        for attr in ("href", "src"):
            if node.has_attr(attr):
                node[attr] = build_llms.urljoin(source, node[attr])
    body = APIConverter(heading_style="ATX", bullets="-", strip=["div"]).convert(str(content))
    return body.strip() + "\n"


def normalize_markdown(text):
    """Use the official Markdown endpoint as the snapshot body."""
    return text.lstrip("\ufeff").replace("\r\n", "\n").strip() + "\n"


def validate_document(body, label, minimum, required):
    # An upstream error page or partial response must not replace the snapshot.
    _, _, _, sections = build_llms.parse_document(body)
    anchors = {section.anchor for section in sections}
    if len(sections) < minimum or not set(required) <= anchors:
        raise ValueError(
            f"Converted {label} document is incomplete; keeping the previous snapshot"
        )


def upsert(source_path, output, body, *, title, url, summary=None,
           minimum=1, required=(), externals=None):
    body = body.strip() + "\n"
    validate_document(body, title, minimum, required)
    old_text = source_path.read_text(encoding="utf-8-sig") if source_path.exists() else ""
    old_body = re.sub(r"\A---\n.*?\n---\n", "", old_text, count=1, flags=re.S).strip()
    if old_body == body.strip():
        text = old_text
    else:
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        metadata = [f"title: {json.dumps(title, ensure_ascii=False)}",
                    f"url: {json.dumps(url, ensure_ascii=False)}"]
        if summary:
            metadata.append(f"summary: {json.dumps(summary, ensure_ascii=False)}")
        metadata.append(f"date: {json.dumps(timestamp)}")
        text = "---\n" + "\n".join(metadata) + "\n---\n\n" + body
    files = build_llms.build(text, externals)
    # Only retire unchanged files that the previous source demonstrably generated.
    old_files = build_llms.build(old_text, externals) if old_text else {}
    for name in old_files.keys() - files.keys():
        path = output / name
        if path.is_file() and path.read_text(encoding="utf-8") == old_files[name]:
            path.unlink()
    source_path.write_text(text, encoding="utf-8", newline="\n")
    for name, value in files.items():
        path = output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8", newline="\n")
    print(f"Updated {len(files) - 2} pages for {title} in {output}")


def update_api(source_path=API_INPUT, output=API_OUTPUT, html=None,
               externals=EXTERNAL_DIR):
    if html is None:
        html = fetch(API_URL, "text/html")
    body = convert_html(html, API_URL)
    mirrors = mirror_external_pages(body, API_URL, externals) if externals else {}
    upsert(source_path, output, body, title="Telegram Bot API", url=API_URL,
           minimum=100, required={"sendmessage", "user", "getupdates", "games"},
           externals=mirrors)


def update_serverless(source_path=SERVERLESS_INPUT, output=SERVERLESS_OUTPUT,
                      markdown=None, externals=EXTERNAL_DIR):
    if markdown is None:
        markdown = fetch(SERVERLESS_MARKDOWN_URL, "text/markdown")
    body = normalize_markdown(markdown)
    mirrors = mirror_external_pages(body, SERVERLESS_URL, externals) if externals else {}
    upsert(source_path, output, body, title="Telegram Serverless", url=SERVERLESS_URL,
           summary=SERVERLESS_SUMMARY, minimum=30,
           required={"handlers", "endpoints", "the-database", "the-sdk",
                     "command-line-interface"},
           externals=mirrors)


def external_markdown(page):
    """Fetch the official Markdown for a linked page, tolerating transient resets."""
    for attempt in range(3):
        try:
            return fetch(f"{page}.md", "text/markdown")
        except HTTPError as error:
            # Some linked pages have no Markdown endpoint; their links stay absolute.
            if error.code == 404:
                return None
            if attempt == 2:
                raise
        except OSError:
            if attempt == 2:
                raise
        time.sleep(1 + attempt)


def mirror_external_pages(text, source, directory=EXTERNAL_DIR):
    """Save the official Markdown of pages linked from the document body."""
    pages = sorted(build_llms.referenced_pages(text.splitlines(), source))
    saved = 0
    for page in pages:
        relative = build_llms.external_relative(page)
        if relative is None:
            continue
        path = directory / relative
        markdown = external_markdown(page)
        if markdown is None:
            continue
        body = normalize_markdown(markdown)
        if not re.search(r"^#\s+\S", body, re.M):
            raise ValueError(f"{page}.md is not Markdown; keeping the previous mirror")
        if path.is_file() and path.read_text(encoding="utf-8") == body:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8", newline="\n")
        saved += 1
    print(f"Updated {saved} of {len(pages)} linked pages in {directory}")
    return build_llms.load_externals(directory)


def update_external_pages(source_path=API_INPUT, directory=EXTERNAL_DIR):
    """Mirror linked pages for an existing snapshot without refreshing it."""
    text = source_path.read_text(encoding="utf-8-sig")
    _, source, _, _ = build_llms.parse_document(text)
    return mirror_external_pages(text, source, directory)


def fetch(url, accept):
    request = Request(url, headers={"User-Agent": "TelegramLLMDocs/1.0", "Accept": accept})
    with urlopen(request, timeout=90) as response:
        return response.read().decode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=API_INPUT)
    parser.add_argument("--output", type=Path, default=API_OUTPUT)
    parser.add_argument("--serverless-input", type=Path, default=SERVERLESS_INPUT)
    parser.add_argument("--serverless-output", type=Path, default=SERVERLESS_OUTPUT)
    parser.add_argument("--externals", type=Path, default=EXTERNAL_DIR,
                        help="Snapshot directory for pages linked from the API reference")
    args = parser.parse_args()
    update_api(args.input, args.output, externals=args.externals)
    update_serverless(args.serverless_input, args.serverless_output,
                      externals=args.externals)


if __name__ == "__main__":
    main()
