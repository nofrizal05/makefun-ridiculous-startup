"""Ridiculous at First Glance, Real by the Second.

Writes exactly one sentence pitching a bizarre startup idea that sounds
like a joke yet makes sense as a real business: trained crows that collect
cigarette butts in city parks, paid in peanuts, while councils pay per
kilo of litter removed. Standard library only.
"""

import os

SENTENCE = (
    "Our trained crows collect cigarette butts in city parks for peanuts, "
    "and councils pay us per kilo because a crow costs less than a street "
    "sweeper's coffee break."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
