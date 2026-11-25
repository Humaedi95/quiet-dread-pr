"""Quiet Dread — a one-line code review comment that approves a PR.

Writes the entry line to /output/entry.txt as required by the
"Two Days of Quiet Dread" bounty (u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018).
"""

import os

ENTRY = (
    "LGTM. The tests pass, the code is fine, and in a hundred years "
    "none of this will matter, but it ships today."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate requires 1-140 characters, a single line, not only whitespace.
MAX_CHARS = 140


def validate(entry: str) -> None:
    """Fail loudly if the entry would not pass the sealed gate."""
    assert 1 <= len(entry) <= MAX_CHARS, f"entry is {len(entry)} chars"
    assert "\n" not in entry, "entry must be a single line"
    assert entry.strip(), "entry must not be only whitespace"


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
