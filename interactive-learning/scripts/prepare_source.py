#!/usr/bin/env python3
"""Normalize simple learning sources into line-numbered Markdown."""

from __future__ import annotations

import argparse
import html
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


def read_txt(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def read_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml_bytes = zf.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paragraphs: list[str] = []
    for para in root.findall(".//w:p", ns):
        pieces: list[str] = []
        for node in para.iter():
            if node.tag == f"{{{ns['w']}}}t" and node.text:
                pieces.append(node.text)
            elif node.tag == f"{{{ns['w']}}}tab":
                pieces.append("\t")
        text = html.unescape("".join(pieces)).strip()
        if text:
            paragraphs.append(text)
    return "\n\n".join(paragraphs)


def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def add_line_numbers(text: str) -> str:
    lines = text.splitlines()
    width = max(4, len(str(len(lines))))
    return "\n".join(f"{i:0{width}d}: {line}" for i, line in enumerate(lines, 1)) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize md/txt/docx source into line-numbered Markdown.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--title", default=None)
    args = parser.parse_args()

    source = args.input
    if not source.exists():
        print(f"Input not found: {source}", file=sys.stderr)
        return 2

    suffix = source.suffix.lower()
    if suffix == ".docx":
        text = read_docx(source)
    elif suffix in {".md", ".markdown", ".txt"}:
        text = read_txt(source)
    else:
        print("Supported input types: .md, .markdown, .txt, .docx", file=sys.stderr)
        return 2

    title = args.title or source.stem
    body = add_line_numbers(normalize(text))
    output = f"# {title}\n\nSource file: `{source.name}`\n\n```text\n{body}```\n"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(output, encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
