def wrap(text, cols):
    lines = []
    # Loop as long as there is text remaining to be wrapped
    while text:
        # Case 1: The remaining text is short enough to fit on one line.
        # This is typically the last segment of the text.
        if len(text) <= cols:
            lines.append(text)
            text = ""  # Mark text as fully consumed
            break  # Exit the loop

        # Case 2: The remaining text is longer than 'cols'. We need to break it.

        # Find the last space within the first (cols + 1) characters of the current text.
        # The search range '0, cols + 1' means indices from 0 up to 'cols' (inclusive of text[cols]).
        # This allows breaking *at* text[cols] if it happens to be a space.
        split_point = text.rfind(" ", 0, cols + 1)

        # Determine the line based on the 'split_point':
        # If 'split_point' is -1 (no space found in the segment)
        # OR if 'split_point' is 0 (meaning the text starts with a space, and the word
        # following it is too long to fit after that space within the 'cols' limit,
        # or there are no other spaces before 'cols' to break on).
        # In these scenarios, we must break the "word" (or block of non-spaces/initial spaces) at 'cols'.
        if split_point <= 0:
            line = text[:cols]
            text = text[cols:]
        else:
            # A space was found at 'split_point' (where 'split_point' is greater than 0).
            # The line should end *before* this space.
            line = text[:split_point]
            # The remaining text starts from this space. This is crucial for
            # preserving the exact amount of spaces as required by the problem,
            # as leading spaces for the next line are explicitly carried over.
            text = text[split_point:]

        # Add the determined line to the list of wrapped lines
        lines.append(line)

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
