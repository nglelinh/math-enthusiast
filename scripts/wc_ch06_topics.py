#!/usr/bin/env python3
"""Word counts for Chapter 06 topic lectures (exclude Overview)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "contents/en/chapter06/_posts"
VI = ROOT / "contents/vi/chapter06/_posts"

EN_FILES = sorted(
    p for p in EN.glob("21-01-01-06_*.md") if "06_00" not in p.name
)
VI_FILES = sorted(
    p for p in VI.glob("21-01-01-06_*.md") if "06_00" not in p.name and "Tong_quan" not in p.name
)


def body_words(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    # strip YAML front matter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    # collapse markdown-ish noise lightly
    text = re.sub(r"\$\$.*?\$\$", " MATH ", text, flags=re.S)
    text = re.sub(r"\{%.*?%\}", " ", text)
    text = re.sub(r"\{\{.*?\}\}", " ", text)
    return len(text.split())


def main() -> None:
    print("EN topic lectures (wc -w style, body after front matter):")
    for p in EN_FILES:
        n = body_words(p)
        flag = "OK" if n >= 1400 else "LOW"
        print(f"  {n:5d}  {flag:3s}  {p.name}")
    print("\nVI topic lectures:")
    for p in VI_FILES:
        n = body_words(p)
        flag = "OK" if n >= 1000 else "LOW"
        print(f"  {n:5d}  {flag:3s}  {p.name}")


if __name__ == "__main__":
    main()
