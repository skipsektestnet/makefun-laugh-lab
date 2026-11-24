"""One-Liner Laugh Lab — writes the entry to /output/entry.txt.

Why this line: it answers the prompt — the excuse a robot vacuum gives
after eating a sock — and the joke comes from the fit. The vacuum does not
apologise; it mounts a legal defence ("the sock came at me first"), then
twists the knife: its dustbin wears the sock better than its owner did. The
turn is deadpan, the image is concrete, and every word works.

The gate wants one line of 1 to 200 characters, UTF-8, not only whitespace.
So the entry is one constant, validated hard before it is written anywhere.
"""

import os

# The entry itself: one line, the vacuum's defence for eating the sock.
# Kept as a named constant so the choice is explicit and checkable.
ENTRY = "In my defence, the sock came at me first, and frankly my dustbin wears it better than you did."

OUTPUT_PATH = "/output/entry.txt"
# The gate allows 1 to 200 characters.
MAX_LENGTH = 200


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert len(text) <= MAX_LENGTH, (
        f"entry must be at most {MAX_LENGTH} chars, got {len(text)}"
    )
    # One line only: the gate reads a single short funny line.
    assert "\n" not in text, "entry must be a single line"
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
