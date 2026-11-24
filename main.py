#!/usr/bin/env python3
"""Sum up 24 November 2026's world news in one image.

Entry program for the make.fun bounty "news-image-20261124".

The finished front page lives beside this file as ``entry.png``: a
1024x1024 PNG that sums up Tuesday 24 November 2026 in one image —
31 verified stories across 9 regions (3 heroes, 10 tiles, 18 wire
briefs), every item date-checked against the day.

Behaviour: copy ``entry.png`` from this file's directory into the
output directory, byte for byte, so the bytes the judge sees are
exactly the bytes committed to the repository. The output directory
is ``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output`` (the
grader's container). No network, no clocks, no randomness: running
the program any number of times always yields the identical file.

Python 3.13, standard library only.
"""

import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def source_image() -> Path:
    """The committed front page, resolved next to this program file."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def output_dir() -> Path:
    """Where the grader wants the image: env override, else /output."""
    return Path(os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR))


def main() -> int:
    src = source_image()
    if not src.is_file():
        print(f"error: {ENTRY_NAME} not found beside main.py", file=sys.stderr)
        return 1

    dest_dir = output_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / ENTRY_NAME

    # Byte-for-byte copy: the committed PNG is the entry, unchanged.
    shutil.copyfile(src, dest)

    size = dest.stat().st_size
    print(f"wrote {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
