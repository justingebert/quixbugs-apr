def wrap(text, cols):
    lines = []
    # Continue slicing off lines until the remaining text is short enough
    while len(text) > cols:
        # Find the last space within the allowed width
        end = text.rfind(" ", 0, cols + 1)
        # If no space found or space is at position 0, break at cols
        if end <= 0:
            end = cols
        # Slice off the line and update the remaining text
        line = text[:end]
        text = text[end:]
        lines.append(line)
    # Append any leftover text as the final line (if non-empty)
    if text:
        lines.append(text)
    return lines


"""
Wrap Text

Given a long string and a column width, break the string on spaces into a list of lines such that each line is no longer than the column width.

Input:
    text: The starting text.
    cols: The target column width, i.e. the maximum length of any single line after wrapping.

Precondition:
    cols > 0.

Output:
    An ordered list of strings, each no longer than the column width, such that the concatenation of the strings returns the original text,
and such that no word in the original text is broken into two parts unless necessary.  The original amount of spaces are preserved (e.g. spaces
at the start or end of each line aren't trimmed.)
"""
