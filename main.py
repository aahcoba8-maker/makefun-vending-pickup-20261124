"""Vending machine pickup line entry for make.fun.

Writes a single pickup line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only.
"""
import os
from pathlib import Path

ENTRY = "Press B7 and I'll drop my sweetest snack for free \u2014 your smile is the only exact change I take."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    out_path.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
