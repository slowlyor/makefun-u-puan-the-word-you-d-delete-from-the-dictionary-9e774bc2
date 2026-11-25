#!/usr/bin/env python3
"""Write the one word to erase from the dictionary to /output/entry.txt.

The word: lisp. A speech impediment named with a word full of the very
sound its sufferers cannot pronounce -- the dictionary's cruelest joke.
Deleting it is the merciful edit.
"""

import os

WORD = "lisp"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify the gate: valid UTF-8, 1-77 chars,
    # exactly one word, nothing else attached.
    with open("/output/entry.txt", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 77, "entry length out of gate range"
    assert text.strip() and len(text.split()) == 1, "entry must be one word"
    assert text == WORD, "entry does not match the chosen word"


if __name__ == "__main__":
    main()
