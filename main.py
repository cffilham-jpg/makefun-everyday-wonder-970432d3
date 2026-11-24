#!/usr/bin/env python3
"""Write one sentence about a small everyday moment of wonder to entry.txt.

The program writes a single sentence (at most 200 characters, no trailing
newline) to ``entry.txt`` inside the output directory named by the
MAKEFUN_OUTPUT_DIR environment variable (default ``out``).
"""

import os

CHAR_LIMIT = 200

SENTENCE = (
    "At 3 a.m. the fridge hum changed key, and for a moment the kitchen "
    "sounded like a room I had never lived in."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    line = SENTENCE
    if len(line) > CHAR_LIMIT:
        raise SystemExit("sentence exceeds 200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("sentence must be a single line")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
