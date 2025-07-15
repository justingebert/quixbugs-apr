def wrap(text, cols):
    lines = []
    while len(text) > cols:
        # Try to find a breaking space within the cols limit.
        # The search range `0, cols + 1` means indices `0` through `cols`.
        space_idx = text.rfind(" ", 0, cols + 1)

        # Determine the `end` point for the current line.
        # Case 1: No space found in text[0...cols] OR the only space found is at text[0].
        # In both these scenarios, we must take the first `cols` characters.
        # This will either break a long word, or include a leading space and break a word.
        # This also prevents an infinite loop if `space_idx` is 0 (as `text[:0]` and `text[0:]` would cause no change to `text`).
        if space_idx == -1 or space_idx == 0:
            end = cols
        # Case 2: A suitable breaking space was found at `space_idx` (> 0).
        # We break at this space to avoid splitting a word unnecessarily.
        else:
            end = space_idx

        # Extract the line and update the remaining text.
        line, text = text[:end], text[end:]
        lines.append(line)

    # After the loop, if any text remains (i.e., its length is <= cols),
    # append it as the last line.
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
at the start or end of each line aren't trimmed.),Wrapping Text
"""
