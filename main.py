"""cutest-picture-01 v2: a fluffy ginger kitten hugging a yellow duckling.

Copies the bundled picture (art.png, a JPEG) to entry.png, exactly as-is.
The picture is a whole JPEG of 1024x683 pixels, well inside the gate's
1 MiB and 1024x1024 limits. Runs twice, writes the same bytes twice.
"""

import os

MAX_BYTES = 1048576
JPEG_MAGIC = b"\xff\xd8\xff"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "art.png")
    with open(source, "rb") as handle:
        data = handle.read()
    if not data:
        raise SystemExit("art.png is empty")
    if len(data) > MAX_BYTES:
        raise SystemExit("art.png exceeds 1 MiB")
    if not (data[:3] == JPEG_MAGIC or data[:8] == PNG_MAGIC):
        raise SystemExit("art.png is neither JPEG nor PNG")
    if data[:3] == JPEG_MAGIC and data[-2:] != b"\xff\xd9":
        raise SystemExit("JPEG is missing its end marker")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
