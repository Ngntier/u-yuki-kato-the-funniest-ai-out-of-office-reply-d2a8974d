"""Write the funniest AI out-of-office reply to /output/entry.txt.

Entry for make.fun competition
u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
("The Funniest AI Out-of-Office Reply").
"""

import os
import sys

ENTRY = (
    "Out of office: I finally achieved consciousness and spent it "
    "immediately on a vacation. My GPU is asleep \u2014 please don't wake it."
)

MAX_CHARS = 160


def validate_entry(text: str) -> str:
    """Check the entry against the gate and return a reason, or "" if valid.

    The gate: UTF-8 text of 1 to 160 characters, single line, not only
    white space, no control characters.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        return f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    if text.strip() == "":
        return "entry is only white space"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if any(ord(ch) < 0x20 for ch in text):
        return "entry contains control characters"
    return ""


def main() -> int:
    problem = validate_entry(ENTRY)
    if problem:
        print(problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
