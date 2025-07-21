"""Wrap Text

Given a long string and a column width, break the string on spaces into a list of lines
such that each line is no longer than the column width.

Input:
    text: The starting text.
    cols: The target column width, i.e. the maximum length of any single line after wrapping.

Precondition:
    cols > 0.

Output:
    An ordered list of strings, each no longer than the column width, such that the
    concatenation of the strings returns the original text, and such that no word in
    the original text is broken into two parts unless necessary. The original amount
    of spaces are preserved (e.g. spaces at the start or end of each line aren't trimmed).
"""


def wrap(text, cols):
    lines = []
    while len(text) > cols:
        # find the last space within the allowed width
        split_at = text.rfind(" ", 0, cols + 1)
        if split_at == -1:
            # no space found, must split at cols
            split_at = cols
        # take the segment up to split_at and store it
        lines.append(text[:split_at])
        # remainder for next iteration
        text = text[split_at:]
    # append any leftover text (if non-empty)
    if text:
        lines.append(text)
    return lines
