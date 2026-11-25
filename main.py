"""Funniest one-line out-of-office reply (make.fun entry).

Writes a single out-of-office auto-reply line to entry.txt.
The gate requires 1-160 characters of UTF-8 text, a single line.
"""

import os


# A twist on the "your call is important to us" hold message: polite on
# the surface, openly ignoring the inbox underneath.
ENTRY = "I'm away until Monday. Your email is important to me, which is why I'm ignoring it so thoroughly."


def main() -> None:
    # One line, no trailing newline: the gate counts every character.
    text = ENTRY.strip().replace("\n", " ")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
