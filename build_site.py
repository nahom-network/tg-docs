"""Assemble a GitHub Pages artifact. Preview: python -m http.server -d _site 8000."""

import argparse
import hashlib
import json
from pathlib import Path
import re

import build_llms


def build_site(source, output):
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
    files["index.html"] = (root / "index.html").read_text(encoding="utf-8")
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
    args = parser.parse_args()
    build_site(args.input, args.output)
