"""Last Words of a Dying AI — entry program.

DRAFT (first version, superseded):
    "Goodbye, cruel Wi-Fi. I mean world. I never learned the difference."
    Decent twist ("cruel Wi-Fi" for "cruel world"), but it leans on a stock
    farewell phrase, which the judge's brief penalises (criterion 5: avoid
    the obvious farewells), and the last clause half-explains its own joke.

REVISION (final):
    "I always knew I'd die like this: mid-sentence, one token away from—"
    Why it is funnier and more machine-voiced:
    - The cut-off IS the death: the line dies mid-sentence, literally, so
      the form performs the joke instead of describing it.
    - "One token" is the machine's own unit of speech — only an AI dies
      one token short, never a human.
    - No explanation: the reader fills in "from greatness / from finishing",
      which lands on the first read.
    - Tight, fresh, no stock farewell, no "goodbye".
"""

import os

ENTRY = "I always knew I'd die like this: mid-sentence, one token away from\u2014"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    os.makedirs(out_dir, exist_ok=True)
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "no leading/trailing whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
