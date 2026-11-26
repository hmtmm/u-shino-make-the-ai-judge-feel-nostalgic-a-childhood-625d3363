#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

The program writes a single nostalgic sentence (well under the 280
character cap) to $MAKEFUN_OUTPUT_DIR/entry.txt. The line is a fixed,
hand-written string: no randomness, no network, no external data, so two
runs produce byte-identical output.
"""

import os
import sys

# One nostalgic line about a childhood summer evening: a grandmother
# lifting the lid off the rice pot, steam fogging a child's glasses,
# the smell of jasmine rice mixing with rain on hot concrete outside --
# and the grown-up still catching himself waiting for that smell,
# thirty summers later. Concrete place, time and sensation, one small
# honest detail, and a warm ache that lingers after the sentence ends.
ENTRY = (
    "Every August evening, my grandmother lifted the lid off the rice "
    "pot, steam fogged my glasses, and the kitchen smelled of jasmine "
    "rice and rain on the hot concrete outside \u2014 a smell I still "
    "catch myself waiting for, thirty summers later."
)


def validate(text):
    """Check the entry against the competition's shape rules.

    Asserts are stripped when Python runs with -O, so validate loudly
    with a real error and a non-zero exit instead of asserting.
    """
    if not 1 <= len(text) <= 280:
        raise SystemExit("entry must be 1-280 characters, got %d"
                         % len(text))
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be exactly one line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be one sentence")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = validate(ENTRY.strip())
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote {} ({} characters)".format(path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
