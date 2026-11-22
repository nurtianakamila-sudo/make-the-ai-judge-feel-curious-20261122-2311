#!/usr/bin/env python3
"""make-the-ai-judge-feel-curious-20261122-2311

Writes a single short text to /output/entry.txt. Deterministic:
no network, no randomness, no timestamps, same bytes on every run.
"""

# Output is capped at 280 Unicode code points by the competition rules; this text is 219.

import os

TEXT = (
    "In 1998, a lighthouse keeper logged a ship that never existed \u2014 "
    "no name, no flag, no crew on deck. Every night since, at exactly "
    "3:12 a.m., the same light blinks twice from the empty sea. "
    "Who is signalling, and to whom?"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
