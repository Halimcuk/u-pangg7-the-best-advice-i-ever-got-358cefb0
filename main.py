"""The Best Advice I Ever Got.

A tiny deterministic program: it writes exactly one sentence about the
best advice the writer ever received to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (or ./output by default).
"""

import os
from pathlib import Path

ENTRY = (
    "My father, wiping grease off his hands after fixing our old truck, "
    "told me to finish what I start, especially when no one is watching."
)


def main() -> None:
    # One sentence, 134 characters: a father's grease-stained advice after
# fixing the old truck. Kept deliberately plain so it reads as a real voice.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
