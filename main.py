"""One-Liner Laugh Lab — the robot vacuum's excuse, as a single line.

The prompt asks for the excuse a robot vacuum gives after eating a sock.
The joke escalates instead of apologising: first a self-defence claim
("the sock started it"), then a custody battle where the dustbin holds
custody and the owner only gets Sunday visitation. Deadpan escalation,
a concrete image, and the punchline lands on the last word.

The gate wants one line of 1 to 200 characters, UTF-8, with visible
content. This module keeps the line, runs it through every gate rule,
and writes it to /output/entry.txt with no trailing newline.
"""

from pathlib import Path

# The vacuum's defence, kept verbatim: exactly 102 characters.
LINE = "The sock started it. I just finished it — and now my dustbin has custody, so visitation is on Sundays."

OUT_FILE = Path("/output/entry.txt")
CHAR_LIMIT = 200


class EntryProblem(ValueError):
    """Raised when the line breaks one of the gate rules."""


def _fail(rule, detail):
    raise EntryProblem(f"{rule}: {detail}")


def _check_not_blank(line):
    if not line or line.isspace():
        _fail("blank", "entry must contain visible characters")


def _check_length(line):
    if len(line) > CHAR_LIMIT:
        _fail("too-long", f"{len(line)} chars exceeds the {CHAR_LIMIT} limit")


def _check_one_line(line):
    if "\n" in line or "\r" in line:
        _fail("multi-line", "entry must fit on a single line")


def _check_no_padding(line):
    if line != line.strip():
        _fail("padding", "entry must not start or end with whitespace")


def _check_no_control(line):
    if any(ord(ch) < 32 for ch in line):
        _fail("control-char", "entry must not contain control characters")


def check_line(line):
    """Run every gate rule over the line, in order."""
    for rule in (
        _check_not_blank,
        _check_length,
        _check_one_line,
        _check_no_padding,
        _check_no_control,
    ):
        rule(line)
    return line


def emit(line):
    """Write the checked line to the output file, exactly as-is."""
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(line, encoding="utf-8")
    print(f"wrote {OUT_FILE} ({len(line)} chars)")


def run():
    """Check the line, then emit it."""
    emit(check_line(LINE))


if __name__ == "__main__":
    run()
