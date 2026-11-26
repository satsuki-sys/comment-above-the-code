#!/usr/bin/env python3
"""Write the entry for make.fun 'The Comment Above the Code'.

Writes one funny, painfully honest comment line to /output/entry.txt.
Stdlib only.
"""

import os

ENTRY = "// This bug is load-bearing. Fix it and the other three fall down."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
