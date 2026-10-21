"""Split the saved Telegram Bot API Markdown into linked LLM documentation.

Usage: python build_llms.py tg-docs.md --output llms-docs
Rebuild: python build_llms.py tg-docs.md --output llms-docs --force
Python 3.10+; no third-party dependencies. The source is never modified.
"""

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
from urllib.parse import unquote, urldefrag, urljoin


SOURCE_URL = "https://core.telegram.org/bots/api"
SUMMARY = "The Bot API is an HTTP-based interface for developing Telegram bots."


@dataclass
class Section:
    level: int
    title: str
    anchor: str
    lines: list[str]
    group: str

    @property
    def path(self):
        return f"sections/{self.anchor}.md"


def slug(title):
    return re.sub(r"[^\w\s-]", "", title.lower()).replace(" ", "-")


def outside_fences(lines):
    """Identify actual headings, not headings in nested Markdown examples."""
    fence = None
    for line in lines:
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, rest = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not rest.strip():
                fence = None
            yield line, False
        else:
            yield line, fence is None


def parse_document(text):
    # Only extract the metadata we need; do not attempt to parse arbitrary YAML.
    text = text.lstrip("\ufeff").replace("\r\n", "\n")
    metadata = ""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end == -1:
            raise ValueError("Unclosed front matter")
        metadata, text = text[4:end], text[end + 5:]

    def field(name, default):
        match = re.search(rf"^{name}:\s*([^\n]+)", metadata, re.M)
        return match.group(1).strip().strip("\"'") if match else default

    title = field("title", "Telegram Bot API")
    source = urldefrag(field("url", SOURCE_URL))[0]
    sections = []
    counts = set()
    active = False
    group = ""
    for line, outside in outside_fences(text.splitlines()):
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line) if outside else None
        if heading:
            level, name = len(heading[1]), heading[2]
            if not active:
                if level != 3 or name != "Recent changes":
                    continue
                active = True
            # The saved website footer is not API documentation.
            if level == 5 and name == "Telegram":
                break
            if level in (3, 4):
                base = slug(name) or "section"
                anchor = base
                number = 0
                while anchor in counts:
                    number += 1
                    anchor = f"{base}-{number}"
                counts.add(anchor)
                if level == 3:
                    group = name
                sections.append(Section(level, name, anchor, [], group))
                continue
        if active:
            sections[-1].lines.append(line)

    if not sections:
        raise ValueError("No Telegram API content found (expected '### Recent changes')")

    # Remove the website's closing message without touching the last API table.
    last = sections[-1].lines
    for index, line in enumerate(last):
        if re.fullmatch(r"-{10,}\s*", line):
            del last[index:]
            break
    return title, source, sections


def rewrite_links(lines, source, targets):
    """Rewrite Markdown destinations only; preserve fenced/inline code verbatim."""
    def destination(match):
        url = match[1]
        resolved = urljoin(source, url)
        page, fragment = urldefrag(resolved)
        target = targets.get(unquote(fragment)) if page == source else None
        if target:
            return "](" + target
        # Root-relative website links otherwise break when hosted locally.
        if url.startswith(("/", "#")):
            return "](" + resolved
        return match[0]

    result = []
    for line, outside in outside_fences(lines):
        if outside:
            # Paired backtick runs protect inline examples containing Markdown.
            parts = re.split(r"(`+)(.*?)\1", line)
            for index in range(0, len(parts), 3):
                parts[index] = re.sub(r"\]\(([^\s)]+)", destination, parts[index])
            line = "".join(
                part if index % 3 != 2 else part + parts[index - 1]
                for index, part in enumerate(parts)
            )
        result.append(line)
    return result


def build(text):
    title, source, sections = parse_document(text)
    targets = {section.anchor: f"{section.anchor}.md" for section in sections}
    # Deeper formatting headings stay with their parent page.
    for section in sections:
        for line, outside in outside_fences(section.lines):
            match = re.match(r"^#{5,6}\s+(.+?)\s*#*\s*$", line) if outside else None
            if match:
                anchor = slug(match[1])
                targets.setdefault(anchor, f"{section.anchor}.md#{anchor}")

    files = {}
    index = [f"# {title}", "", f"> {SUMMARY}", "",
             f"Source: {source}", "",
             "Snapshot of the supplied Markdown, not a live API reference.",
             "Read the relevant section and follow its local type/method links.", "",
             "## Full reference", "",
             "- [Complete documentation](llms-full.txt): All API sections in one file."]
    full = [f"# {title}", "", f"> {SUMMARY}", "", f"Source: {source}", ""]
    full_targets = {anchor: f"sections/{target}" for anchor, target in targets.items()}
    for position, section in enumerate(sections):
        if section.level == 3:
            index.extend(["", f"## {section.title}", ""])
        body = "\n".join(rewrite_links(section.lines, source, targets)).strip()
        page = [f"# {section.title}", "", f"Source: {source}#{section.anchor}",
                "", "[Documentation index](../llms.txt)", "", body]
        children = []
        if section.level == 3:
            for child in sections[position + 1:]:
                if child.level == 3:
                    break
                children.append(f"- [{child.title}]({child.anchor}.md)")
        if children:
            page.extend(["", "## In this section", "", *children])
        files[section.path] = "\n".join(page).rstrip() + "\n"
        description = next((line.strip("> ").rstrip("\\") for line in section.lines
                            if line.strip() and not line.startswith(("|", "#", "```", "~~~"))), "")
        description = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", description)
        description = re.sub(r"[*`_]", "", description)
        description = re.sub(r"\s+", " ", description)[:180]
        index.append(f"- [{section.title}]({section.path})" + (f": {description}" if description else ""))
        full.extend([f"{'#' * (section.level - 1)} {section.title}", "",
                     "\n".join(rewrite_links(section.lines, source, full_targets)).strip(), ""])
    files["llms.txt"] = "\n".join(index) + "\n"
    files["llms-full.txt"] = "\n".join(full).rstrip() + "\n"
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", nargs="?", type=Path, default=Path("tg-docs.md"))
    parser.add_argument("--output", type=Path, default=Path("llms-docs"))
    parser.add_argument("--force", action="store_true", help="Overwrite generated paths; never delete other files")
    args = parser.parse_args()
    try:
        files = build(args.input.read_text(encoding="utf-8-sig"))
        paths = [args.output / name for name in files]
        if args.input.resolve() in [path.resolve() for path in paths]:
            raise ValueError("Output would overwrite the input file")
        if not args.force and any(path.exists() for path in paths):
            raise ValueError("Output files already exist; use --force to rebuild or choose another --output")
        for name, content in files.items():
            path = args.output / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Error: {error}\n")
    print(f"Created {len(files) - 2} Markdown pages, llms.txt, and llms-full.txt in {args.output}")


if __name__ == "__main__":
    main()
