#!/usr/bin/env python3
"""Word counts for chapter 04 topic posts (EN and VI)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "contents/en/chapter04/_posts"
VI = ROOT / "contents/vi/chapter04/_posts"

TOPIC_EN = [
    "21-01-01-04_02_Infinity.md",
    "21-01-01-04_03_Fractals.md",
    "21-01-01-04_04_Symmetry.md",
    "21-01-01-04_05_Chaos.md",
    "21-01-01-04_06_Strange_Geometry.md",
    "21-01-01-04_07_Paradoxes.md",
    "21-01-01-04_08_Higher_Dimensions.md",
    "21-01-01-04_09_Minimal_Surfaces.md",
    "21-01-01-04_10_Tilings.md",
    "21-01-01-04_11_Impossible_Shapes.md",
    "21-01-01-04_12_Emergence.md",
]


def body_words(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    # strip YAML front matter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    # strip liquid/math noise lightly for fairer count
    text = re.sub(r"\{\{[^}]+\}\}", " ", text)
    text = re.sub(r"\$\$[^$]*\$\$", " MATH ", text, flags=re.S)
    words = re.findall(r"[A-Za-zÀ-ỹ0-9']+", text)
    return len(words)


def main() -> None:
    print("=== EN chapter04 topics (body words) ===")
    for name in TOPIC_EN:
        p = EN / name
        n = body_words(p)
        flag = " OK" if n >= 1400 else " LOW"
        print(f"{n:5d}{flag}  {p}")
    print("\n=== VI chapter04 topics (body words) ===")
    for name in TOPIC_EN:
        p = VI / name
        if not p.exists():
            # Vietnamese titles may share English filenames
            print(f"MISSING  {p}")
            continue
        n = body_words(p)
        flag = " OK" if n >= 1000 else " LOW"
        print(f"{n:5d}{flag}  {p}")


if __name__ == "__main__":
    main()
