#!/usr/bin/env python3
"""food-picture-01: write one picture of food to /output/entry.png.

The picture is a steaming bowl of premium tonkotsu ramen (entry.png,
bundled with this program). The program copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png and verifies the size.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    assert size <= 1_048_576, f"entry.png too large: {size} bytes (limit 1 MiB)"
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
