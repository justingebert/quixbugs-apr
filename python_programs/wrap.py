def wrap(text, cols):
    lines = []
    # Loop until all text is processed
    while text:
        # 1. If the remaining text fits within the column limit, add it as the last line and finish.
        if len(text) <= cols:
            lines.append(text)
            break

        # 2. Try to find a natural break point (a space) within the column limit.
        #    We search for the last space character in the segment of text
        #    from index 0 up to and including index 'cols'.
        #    The `rfind` method's `end` parameter is exclusive, so `cols + 1` is used
        #    to search up to `text[cols]`.
        split_at = text.rfind(" ", 0, cols + 1)

        # Scenario A: A space was found within the limit.
        if split_at != -1:
            # If the space found is at index 0, it means the current segment of text
            # starts with a space, and potentially no other suitable break point
            # was found within the 'cols' limit.
            # Example: text = " word_longer_than_cols", cols = 5. rfind finds 0.
            # In this case, we should take the leading space as a line,
            # and then continue processing the rest of the text.
            # This prevents an infinite loop or appending an empty string.
            if split_at == 0:
                line = text[0]  # Take the single leading space as a line.
                text = text[1:]  # Remove the taken space from the text.
                lines.append(line)
                continue  # Go to the next iteration to process the remaining text.
            else:
                # Normal case: a space was found at 'split_at' (which is > 0).
                # The line will be the text up to this space.
                # The remaining text starts from this space, preserving it for the next line
                # as per the requirement "spaces at the start or end of each line aren't trimmed".
                line = text[:split_at]
                text = text[split_at:]
                lines.append(line)
        # Scenario B: No space was found within the first 'cols + 1' characters.
        # This typically means the first "word" in the current segment is longer than 'cols'.
        # In this situation, we must break the word as necessary.
        else:
            line = text[:cols]  # Take exactly 'cols' characters.
            text = text[cols:]  # The rest remains for further processing.
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
