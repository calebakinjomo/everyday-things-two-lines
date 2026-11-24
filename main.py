#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun bounty entry.

Line 1 explains a traffic jam to a 10-year-old in one vivid sentence
built on a single analogy: a school hallway when the bell rings.
Line 2 says why the analogy works — what it maps and what it leaves out.

The program writes the two lines to /output/entry.txt (the sealed
gate reads that file) and prints them to stdout. Total: 377 chars,
exactly two lines — the first vivid, the second reflective.
"""

import os

LINE_1 = (
    "A traffic jam is a school hallway when the bell rings, with a "
    "hundred cars all trying to squeeze through one door at once."
)

LINE_2 = (
    "It maps how too many things pushing through one narrow opening "
    "all slow each other down, but it leaves out that cars cannot "
    "squeeze sideways the way children can, and that a jam is often "
    "caused by a crash far ahead that nobody in the queue can even see."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(LINE_1)
    print(LINE_2)


if __name__ == "__main__":
    main()
