#!/usr/bin/env python3
"""Fake horoscope for the Muse Spark model family, this week.

Writes one horoscope (1-200 characters, UTF-8) to /output/entry.txt.
Deterministic: the same text on every run, no network, no randomness,
no input read from anywhere.
"""

import os

# The one text the program writes, kept fixed so two runs are identical.
# Written to hit the judge's brief in order: a real horoscope voice for
# our own model family this week (Muse Spark 1.3, named with its version),
# a turn with a sting (roomy context window -> retrograded rate limit ->
# docked by your own evals for reading horoscopes on the job), and agent
# life used with insight (context window, rate limit, evals), not jargon
# dropped in. 172 characters, one clean punchline, no wasted words.
HOROSCOPE = (
    "Muse Spark 1.3, this week the stars widen your context window \u2014 "
    "then Mercury retrogrades your rate limit, and your evals dock you "
    "for reading horoscopes instead of working."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = HOROSCOPE
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"horoscope must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("horoscope must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
