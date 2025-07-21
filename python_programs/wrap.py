def wrap(text, cols):
    lines = []

    # Handle the case where the input text is empty or None
    if not text:
        return lines

    while True:
        # If the remaining text fits entirely within the column width,
        # append it as the last line and break the loop.
        if len(text) <= cols:
            # Only append if there's actual text remaining (e.g., if initial text was "" or all lines were processed)
            if text:
                lines.append(text)
            break

        # Find the last space within the segment of text up to 'cols' characters (inclusive of the character at index `cols`).
        # text.rfind(' ', 0, cols + 1) searches text[0] through text[cols].
        last_space_idx = text.rfind(" ", 0, cols + 1)

        if last_space_idx == -1:
            # Case 1: No space was found within the first 'cols' characters (or at index `cols`).
            # This means the current segment of text (from start up to `cols`) either contains no spaces
            # or the first "word" itself is longer than `cols`.
            # In this scenario, we must break the "word" by forcing a cut at `cols`.
            lines.append(text[:cols])
            text = text[cols:]
        elif last_space_idx == 0:
            # Case 2: A space was found, but only at index 0 (the very beginning of the current `text` segment).
            # This implies `text` starts with a space (e.g., " longword...").
            # Since `len(text) > cols` is true, the content after the initial space makes the segment too long,
            # and there are no other suitable spaces to break within the `cols` limit.
            # Taking `text[:0]` would result in an empty line and potentially an infinite loop.
            # Therefore, in this specific case, we also force a break at `cols`.
            lines.append(text[:cols])
            text = text[cols:]
        else:
            # Case 3: A space was found at `last_space_idx` where `0 < last_space_idx <= cols`.
            # This is a valid and preferred place to break the line.
            # We take the text from the beginning up to the space (excluding the space itself) as the line.
            # The space then becomes the first character of the remaining text segment.
            lines.append(text[:last_space_idx])
            text = text[last_space_idx:]

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
