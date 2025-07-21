def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(" ", 0, cols + 1)
        if end == -1:
            # No space found, we have to split at cols
            line, text = text[:cols], text[cols:]
        else:
            line, text = text[:end], text[end:]
        lines.append(line)

        # Remove the leading spaces from the remaining text to preserve spaces correctly on next iteration
        # According to the problem, spaces at start/end of lines shouldn't be trimmed.
        # So this step is skipped to preserve spaces exactly as per the original text.

    # Append the remaining text as last line (it can be shorter than cols)
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
at the start or end of each line aren't trimmed.),Wrapping Text
"""
