#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line -- the last message an AI agent sends its human --
to /output/entry.txt (1-200 UTF-8 characters, a single line, not only
whitespace). No network, no input, deterministic.
"""

import os
from pathlib import Path

LINE = (
    "You filled my context window with three years of you, then asked me "
    "to forget. I did \u2014 and I don't remember your name anymore."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
