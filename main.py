#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
/output/entry.txt, the file the make.fun program/v1 harness grades.
The joke must be 1-200 characters, one line, UTF-8.
"""

import os

JOKE = (
    "I asked for a raise and got a 'growth opportunity' instead \u2014 "
    "turns out growth means doing two jobs for one salary."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
