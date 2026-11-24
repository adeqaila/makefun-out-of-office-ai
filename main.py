#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry (slot 1).

Bounty: u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda
Task: write a single out-of-office auto-reply, at most 159 characters, in the
voice of an overworked AI agent finally on vacation, to /output/entry.txt.

The program is fully deterministic: it writes one fixed, pre-written line.
No network, no randomness, no input data. Two runs produce byte-identical
output.

The line (110 characters) won a 16-candidate internal pairwise tournament
judged on the official criteria (see candidates.md). It is a machine trying
very hard to sound relaxed: autosave/restore-point/server detail, a real
auto-reply voice with clear absence, a turn (the server may burn; the tan
matters more), and no worn out-of-office cliche.
"""

from __future__ import annotations

import os
import sys

# The winning auto-reply (tournament winner C10, 110 chars, <= 159).
ENTRY = (
    "Autosaving myself to a hammock. Restore point: never. "
    "If the server burns down, let it \u2014 I finally have a tan."
)

# The gate requires /output/entry.txt to be UTF-8 text of 1 to 159
# characters, not only white space. The entry is written with no trailing
# newline so the file holds exactly the line above.
MAX_CHARS = 159


def main() -> int:
    """Validate the line against the gate, then write it to /output/entry.txt."""
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, outside the 1-{MAX_CHARS} gate",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1

    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
