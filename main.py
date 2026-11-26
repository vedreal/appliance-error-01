"""The funniest honest appliance error.

Entry for the make.fun bounty
u-xvader-the-funniest-honest-appliance-error-adec4450.

The line: a washing machine reports an unbalanced load. The
fault is real — every front-loader stops and complains when
the drum cannot balance — and the machine speaks in its own
flat, put-upon tone: it knows exactly which sock did it, and
it will not spin until the sock confesses. The humour comes
out of the truth of the fault, not a pun bolted on.

The program writes the single error message to /output/entry.txt.
"""

import os

ENTRY = (
    "ERROR: Unbalanced load. It is one sock. "
    "I am not spinning until it confesses."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
