#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner about a hilariously useless
superpower to /output/entry.txt. Standard library only, no network,
fully deterministic: every run writes the exact same bytes.
"""

import os

LINE = "I can teleport anywhere in the world, as long as it's this room."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows one line of 1-200 characters: fail loudly here
    # rather than writing an entry the scorer would mark invalid.
    if "\n" in LINE or "\r" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError("LINE must be one line of 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
