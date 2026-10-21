"""Fetch the official HTML, convert the API content, then rebuild LLM files."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import re
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

import build_llms


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


def convert_html(html):
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
                node[attr] = build_llms.urljoin(build_llms.SOURCE_URL, node[attr])
    body = APIConverter(heading_style="ATX", bullets="-", strip=["div"]).convert(str(content))
    body = body.strip() + "\n"
    # An upstream error page or partial response must not replace the snapshot.
    _, _, sections = build_llms.parse_document(body)
    anchors = {section.anchor for section in sections}
    if len(sections) < 100 or not {"sendmessage", "user", "getupdates", "games"} <= anchors:
        raise ValueError("Converted API document is incomplete; keeping the previous snapshot")
    return body


def update(source_path, output, html):
    body = convert_html(html)
    old_text = source_path.read_text(encoding="utf-8-sig") if source_path.exists() else ""
    old_body = re.sub(r"\A---\n.*?\n---\n", "", old_text, count=1, flags=re.S).strip()
    if old_body == body.strip():
        text = old_text
    else:
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        text = ("---\n" + 'title: "Telegram Bot API"\n'
                + f'url: "{build_llms.SOURCE_URL}"\n'
                + f'date: "{timestamp}"\n' + "---\n\n" + body)
    files = build_llms.build(text)
    # Only retire unchanged files that the previous source demonstrably generated.
    old_files = build_llms.build(old_text) if old_text else {}
    for name in old_files.keys() - files.keys():
        path = output / name
        if path.is_file() and path.read_text(encoding="utf-8") == old_files[name]:
            path.unlink()
    source_path.write_text(text, encoding="utf-8", newline="\n")
    for name, value in files.items():
        path = output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8", newline="\n")
    print(f"Updated {len(files) - 2} API pages from {build_llms.SOURCE_URL}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("tg-docs.md"))
    parser.add_argument("--output", type=Path, default=Path("llms-docs"))
    args = parser.parse_args()
    request = Request(build_llms.SOURCE_URL, headers={"User-Agent": "TelegramLLMDocs/1.0", "Accept": "text/html"})
    with urlopen(request, timeout=90) as response:
        html = response.read().decode("utf-8")
    update(args.input, args.output, html)


if __name__ == "__main__":
    main()
