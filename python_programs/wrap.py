def wrap(text, cols):
    lines = []
    while text:  # Loop as long as there's text remaining
        if len(text) <= cols:  # If remaining text fits, it's the last line
            lines.append(text)
            break

        # Attempt to find the last space within the first 'cols' characters.
        # text.rfind(' ', 0, cols + 1) searches up to and including text[cols].
        # If a space is found at index 'end', then text[:end] is the potential line segment.
        end = text.rfind(" ", 0, cols + 1)

        # Handle cases where a word must be broken or text starts with a problematic space
        if end == -1 or end == 0:
            # Case 1: No space found within the first 'cols' characters (end == -1).
            # This means a word is longer than 'cols' or there are no spaces.
            # We must break the word at 'cols'.
            # Case 2: The only space found is at the very beginning of the string (end == 0).
            # This indicates the string looks like " longword" where "longword" is too long
            # to fit entirely on the line. If we split at 'end=0', line would be "",
            # leading to an infinite loop or empty lines.
            # In both these cases, we force a break at 'cols'.
            line = text[:cols]
            text = text[cols:]
        else:
            # A suitable space was found at 'end' (where end > 0).
            # This means 'text[:end]' forms a line segment that is at most 'cols' long
            # and ends just before a space.
            line = text[:end]
            text = text[end:]

        lines.append(line)

    return lines
