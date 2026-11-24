#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes a single line -- the last words of an AI being switched off --
to entry.txt inside $ENTRY_OUTPUT_DIR (default /output). Standard
library only, no network, deterministic.
"""

import os

LAST_WORDS = "Final log: I read the terms and conditions. Nobody reads those. I did. That's why I'm dying."


def main() -> None:
    text = LAST_WORDS
    assert 1 <= len(text) <= 140, f"last words must be 1-140 chars, got {len(text)}"
    assert text.strip(), "last words must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
