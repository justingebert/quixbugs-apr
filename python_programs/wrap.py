def wrap(text, cols):
    lines = []
    # Loop as long as there is text remaining to be processed
    while text:
        # If the remaining text length is less than or equal to `cols`,
        # it can be added as the last line, and we are done.
        if len(text) <= cols:
            lines.append(text)
            break

        # Try to find the last space within the current column width limit.
        # `rfind(' ', 0, cols + 1)` searches for a space from index 0 up to `cols` (inclusive of `text[cols]`).
        end = text.rfind(" ", 0, cols + 1)

        if end == -1:
            # Case 1: No space was found within the first `cols` characters (or up to text[cols]).
            # This means the current segment starts with a word that is longer than or equal to `cols`,
            # or it's a very long word that needs to be broken.
            # We must break the word by taking exactly `cols` characters.
            line = text[:cols]
            text = text[cols:]
        elif end == 0:
            # Case 2: The only space found within the `cols` limit is at the very beginning of the `text` (`text[0]`).
            # This indicates `text` starts with a space, and no other space for a graceful break was found
            # within the first `cols` characters after that leading space.
            # To prevent an infinite loop (since `text[:0]` is empty and `text[0:]` is the original text),
            # we must consume at least `text[0]` (the leading space).
            # The problem explicitly states spaces should be preserved, so placing it on its own line is valid.
            line = text[0]  # Take the leading space as the line
            text = text[1:]  # Advance text past the leading space
        else:
            # Case 3: A valid space was found at `end` (where `end > 0`).
            # This is a good place to break the line.
            # `text[:end]` contains the content up to, but not including, the space.
            # `text[end:]` contains the space and the rest of the text.
            # This handles line breaks between words while potentially preserving leading spaces for the next line.
            line = text[:end]
            text = text[end:]

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
