#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review from a house cat about its
human to /output/entry.txt. Deterministic, standard library only, no network.
"""

import os

REVIEW = (
    "One star. I sat on his laptop to help him type and he moved me. "
    "Twice. The keyboard is mine now; the human is under review."
)


def main() -> None:
    assert 0 < len(REVIEW) <= 200, "REVIEW must be non-empty and within the 200-char contest limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
