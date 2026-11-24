#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes a single line, at most 120 characters: the error message a kitchen
toaster shows its owner when something goes wrong.
"""

import os

ENTRY = "ERROR: BREAD JAMMED. I HAVE ALREADY WRITTEN MY RESIGNATION LETTER."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    if len(line) > 120:
        raise SystemExit(f"entry line is {len(line)} characters, over the 120 limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
