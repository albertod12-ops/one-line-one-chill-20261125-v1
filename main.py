"""One Line, One Chill - v1.

Writes a single horror sentence to /output/entry.txt.
Deterministic, stdlib only, no network, no reads outside the repo.
"""

import os

LINE = "Two sets of footprints left my cabin in the fresh snow this morning; I live alone, and only one set came back."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
