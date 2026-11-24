"""Last text at one percent battery, in the dying phone's own voice."""

import os

# Judging trade-off (T4): the joke is the phone dying mid-word on "and" —
# the most filler word, mid-story, so the big reveal is lost forever.
# No explicit "phone"/"1%": the brief already frames every entry as a
# dying phone's text, and naming it would blunt the punch. T4 tried three
# alternatives (wasted-it-on-"anyway", charger farewell, died-mid-"senten");
# none beat this line — the first two needed a non-ASCII em-dash, the third
# is the obvious version of the same trick with "1%" spelled out.
ENTRY = 'I was going to send the full story, but my screen just dimmed during the word "and."'

assert (
    1 <= len(ENTRY) <= 200
    and ENTRY.strip() == ENTRY
    and "\n" not in ENTRY
    and "\r" not in ENTRY
    and all(ord(c) < 128 for c in ENTRY)  # plain ASCII per brief
), "entry must be one line, 1-200 chars, plain ASCII, no stray whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
