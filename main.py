#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

The program writes a single nostalgic sentence (well under the 280
character cap) to $MAKEFUN_OUTPUT_DIR/entry.txt. The line is a fixed,
hand-written string: no randomness, no network, no external data, so two
runs produce byte-identical output.
"""

import os

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


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote {} ({} characters)".format(path, len(text)))


if __name__ == "__main__":
    main()
