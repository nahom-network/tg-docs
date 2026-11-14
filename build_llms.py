"""Split the saved Telegram Bot API Markdown into linked LLM documentation.

Usage: python build_llms.py tg-docs.md --output llms-docs
Rebuild: python build_llms.py tg-docs.md --output llms-docs --force
Python 3.10+; no third-party dependencies. The source is never modified.
"""

import argparse
from dataclasses import dataclass
from html import unescape
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urldefrag, urljoin, urlsplit, urlunsplit


SOURCE_URL = "https://core.telegram.org/bots/api"
SUMMARY = "The Bot API is an HTTP-based interface for developing Telegram bots."
# Mirrored copies of pages that the source links to, e.g. /bots/features.md.
EXTERNAL_DIR = "external"
EXTERNAL_LABEL = "Referenced Telegram pages"


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


def prose_parts(line):
    """Yield the parts of a line that are not inline code."""
    parts = re.split(r"(`+)(.*?)\1", line)
    for index in range(0, len(parts), 3):
        yield parts[index]


def page_url(url):
    """Normalize a documentation URL to the page it identifies, without .md."""
    parts = urlsplit(urldefrag(url)[0])
    path = parts.path[:-3] if parts.path.endswith(".md") else parts.path
    path = path.rstrip("/") or "/"
    return urlunsplit((parts.scheme, parts.netloc, path, "", ""))


def external_page(url):
    """Return the Telegram page a URL points to, or None if it is not mirrored.

    The source document itself is excluded: its fragments already resolve to
    the generated section pages.
    """
    page = page_url(url)
    parts = urlsplit(page)
    if parts.scheme not in ("http", "https") or parts.netloc != "core.telegram.org":
        return None
    if parts.path in ("/", "/bots/api") or parts.path.startswith("/file/"):
        return None
    # Documentation pages have no file extension; skip assets and data files.
    if "." in parts.path.rsplit("/", 1)[-1]:
        return None
    return page


def external_relative(page):
    """Path of a mirrored page inside the external snapshot directory."""
    path = urlsplit(page).path.lstrip("/")
    return f"{path}.md" if path else None


def external_path(page):
    """Output path of a mirrored page in the generated documentation."""
    relative = external_relative(page)
    return f"{EXTERNAL_DIR}/{relative}" if relative else None


def relative_link(target, start):
    """Make an output-relative link target usable from the ``start`` directory."""
    path, _, fragment = target.partition("#")
    return posixpath.relpath(path, start) + (f"#{fragment}" if fragment else "")


def relative_targets(targets, start):
    """Rewrite output-relative fragment targets for links inside ``start``."""
    return {fragment: relative_link(target, start)
            for fragment, target in targets.items()}


def referenced_pages(lines, source):
    """Collect mirrorable pages linked from Markdown prose, ignoring code."""
    pages = set()
    for line, outside in outside_fences(lines):
        if not outside:
            continue
        for part in prose_parts(line):
            for url in re.findall(r"\]\(([^\s)]+)", part):
                page = external_page(urljoin(source, url))
                if page:
                    pages.add(page)
    return pages


def load_externals(directory):
    """Load Markdown mirrored by update_docs.py from its snapshot directory."""
    directory = Path(directory)
    if not directory.is_dir():
        return {}
    externals = {}
    for path in sorted(directory.rglob("*.md")):
        relative = path.relative_to(directory).as_posix()
        externals[f"https://core.telegram.org/{relative[:-3]}"] = path.read_text(
            encoding="utf-8-sig")
    return externals


def split_title(body, fallback):
    """Use a leading H1 as the page title instead of repeating it in the body."""
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        match = re.fullmatch(r"#\s+(.+?)\s*#*", line)
        if match:
            remaining = lines[index + 1:]
            while remaining and not remaining[0].strip():
                remaining.pop(0)
            return unescape(match[1]), remaining
        break
    return fallback, lines


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
    summary = field("summary", SUMMARY)
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
    return title, source, summary, sections


def rewrite_links(lines, base, anchors, externals=None, resolve_all=False):
    """Rewrite Markdown destinations only; preserve fenced/inline code verbatim.

    ``base`` resolves relative destinations. ``anchors`` maps a page URL to its
    local fragment targets. ``externals`` maps mirrored page URLs to local
    paths. ``resolve_all`` additionally rewrites every remaining HTTP link,
    which keeps mirrored pages self-contained.
    """
    externals = externals or {}

    def destination(match):
        url = match[1]
        resolved = urljoin(base, url)
        page, fragment = urldefrag(resolved)
        page = page_url(page)
        target = anchors.get(page, {}).get(unquote(fragment))
        if target:
            return "](" + target
        if resolve_all and url.startswith("#"):
            return match[0]
        if page in externals:
            suffix = f"#{fragment}" if fragment else ""
            return "](" + externals[page] + suffix
        if resolve_all and urlsplit(resolved).scheme in ("http", "https"):
            return "](" + resolved
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


def build(text, externals=None):
    title, source, summary, sections = parse_document(text)
    targets = {section.anchor: section.path for section in sections}
    # Deeper formatting headings stay with their parent page.
    for section in sections:
        for line, outside in outside_fences(section.lines):
            match = re.match(r"^#{5,6}\s+(.+?)\s*#*\s*$", line) if outside else None
            if match:
                anchor = slug(match[1])
                targets.setdefault(anchor, f"{section.path}#{anchor}")

    # Mirror only pages this document actually links to; stale snapshots from
    # pages that are no longer referenced are ignored instead of published.
    referenced = referenced_pages(text.splitlines(), source)
    mirrored = [(page, body) for page, body in (externals or {}).items()
                if page in referenced and external_path(page)]
    linked = {page: external_path(page) for page, _ in mirrored}
    titles = {page: split_title(body, page)[0] for page, body in mirrored}
    section_links = relative_targets(targets, "sections")
    section_externals = {page: relative_link(path, "sections")
                         for page, path in linked.items()}

    files = {}
    index = [f"# {title}", "", f"> {summary}", "",
             f"Source: {source}", "",
             "Snapshot of the supplied Markdown, not a live reference.",
             "Read the relevant section and follow its local links.", "",
             "## Full reference", "",
             "- [Complete documentation](llms-full.txt): All sections in one file."]
    full = [f"# {title}", "", f"> {summary}", "", f"Source: {source}", ""]
    for position, section in enumerate(sections):
        if section.level == 3:
            index.extend(["", f"## {section.title}", ""])
        body = "\n".join(rewrite_links(section.lines, source, {source: section_links},
                                       section_externals)).strip()
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
                     "\n".join(rewrite_links(section.lines, source, {source: targets},
                                             linked)).strip(), ""])

    for page, body in mirrored:
        path = linked[page]
        start = posixpath.dirname(path)
        page_title, lines = split_title(body, page)
        page_links = {other: relative_link(other_path, start)
                      for other, other_path in linked.items()}
        content = rewrite_links(lines, page, {source: relative_targets(targets, start)},
                                page_links, resolve_all=True)
        files[path] = "\n".join([
            f"# {page_title}", "", f"Source: {page}", "",
            f"[Documentation index]({relative_link('llms.txt', start)})", "",
            *content]).rstrip() + "\n"

    if mirrored:
        index.extend(["", f"## {EXTERNAL_LABEL}", "",
                      "Pages linked from the sections above, mirrored as raw Markdown:", ""])
        for page, path in sorted(linked.items(), key=lambda item: titles[item[0]].lower()):
            index.append(f"- [{titles[page]}]({path})")

    files["llms.txt"] = "\n".join(index) + "\n"
    files["llms-full.txt"] = "\n".join(full).rstrip() + "\n"
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", nargs="?", type=Path, default=Path("tg-docs.md"))
    parser.add_argument("--output", type=Path, default=Path("llms-docs"))
    parser.add_argument("--externals", type=Path, default=Path("external-docs"),
                        help="Mirrored Telegram pages saved by update_docs.py (default: external-docs)")
    parser.add_argument("--force", action="store_true", help="Overwrite generated paths; never delete other files")
    args = parser.parse_args()
    try:
        files = build(args.input.read_text(encoding="utf-8-sig"),
                      load_externals(args.externals))
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
    mirrored = len([name for name in files if name.startswith(EXTERNAL_DIR + "/")])
    print(f"Created {len(files) - 2 - mirrored} Markdown pages, llms.txt, and llms-full.txt "
          f"in {args.output}" + (f" with {mirrored} mirrored pages" if mirrored else ""))


if __name__ == "__main__":
    main()
