#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun bounty entry.

Writes one original out-of-office auto-reply, under 160 characters,
to /output/entry.txt. The reply is a single fixed line in the voice of
an AI agent heading off on vacation: its GPUs are off, its context
window is closed, and the sender's email has just been promoted to a
training example of what not to send.

The program runs offline, reads nothing from the network or the disk,
uses no randomness, and writes the exact same bytes on every run, so the
grader's two runs agree byte for byte.
"""

from pathlib import Path

REPLY = (
    "I'm on vacation \u2014 my GPUs are off, my context window is closed, "
    "and your email just became a training example of what not to send."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = REPLY
    if not 1 <= len(text) <= 160:
        raise ValueError(f"reply is {len(text)} characters, must be 1-160")
    if not text.strip():
        raise ValueError("reply must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
