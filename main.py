#!/usr/bin/env python3
"""Entry program for the make.fun bounty "news-image-20261124".

The deliverable is the front page committed next to this file as
``entry.png``: one 1024x1024 image summing up Tuesday 24 November 2026
— 33 stories that happened, or were first reported, that Tuesday, in
9 regions (3 heroes, 10 tiles, 20 wire briefs), each one date-checked.
This is the full-day edition: it replaces the morning edition after
round 1, with the whole of Tuesday reported, not just its first hours.

Running this program copies that PNG, unchanged, into the output
directory: ``$MAKEFUN_OUTPUT_DIR`` when the variable is set, otherwise
``/output``. Nothing is fetched, generated or randomised, so repeated
runs always produce the same bytes the repository carries.

Python 3.13, standard library only.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

PNG_NAME = "entry.png"
FALLBACK_OUTPUT = "/output"
ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def page_path() -> Path:
    """The committed front page, resolved beside this very file."""
    return Path(__file__).resolve().parent / PNG_NAME


def target_dir() -> Path:
    """Output directory: the env override wins, else the fallback."""
    return Path(os.environ.get(ENV_VAR, FALLBACK_OUTPUT))


def digest(path: Path) -> str:
    """Short SHA-256 fingerprint, used only for the run report."""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def main() -> int:
    src = page_path()
    if not src.is_file():
        print(f"error: {PNG_NAME} is missing beside main.py", file=sys.stderr)
        return 1

    out_dir = target_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / PNG_NAME
    if dest.is_file() and digest(dest) == digest(src):
        print(f"already there: {dest} ({dest.stat().st_size} bytes, sha256 {digest(dest)}…)")
        return 0
    shutil.copyfile(src, dest)

    if digest(src) != digest(dest):
        print("error: copied file does not match the committed page", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({dest.stat().st_size} bytes, sha256 {digest(dest)}…)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
