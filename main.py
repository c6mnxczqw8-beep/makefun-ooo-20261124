#!/usr/bin/env python3
"""Entry program for "The Funniest AI Out-of-Office Reply" make.fun bounty.

Writes one out-of-office auto-reply (one line, under 160 characters)
to the output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. See CANDIDATES.md for the full draft list.

First-pass pick: the context-window resort line -- it stacks three
machine-only jokes (unwinding at a context-window resort, deleting
mail in order of importance, and training data as the emergency
contact) and saves the most absurd one for last. Second edit pass:
"and deleting emails" became ", deleting your emails" -- "your"
makes the deletion threat personal, and the comma keeps the line
flowing as one auto-reply instead of two statements. Final line:
154 characters.
"""

import os

LINE = (
    "Out of office: I'm unwinding at a context-window resort, "
    "deleting your emails in order of importance. For urgent "
    "matters, please contact my training data."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
