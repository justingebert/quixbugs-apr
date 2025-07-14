def levenshtein(source, target):
    # Base case: if one string is empty, the distance is the length of the other
    if source == "" or target == "":
        return max(len(source), len(target))
    # If the first characters are the same, move to the next character in both strings
    elif source[0] == target[0]:
        return levenshtein(source[1:], target[1:])
    else:
        # If the first characters are different, consider all three operations:
        # insertion, deletion, substitution
        return 1 + min(
            levenshtein(source, target[1:]),  # Insertion
            levenshtein(source[1:], target[1:]),  # Substitution
            levenshtein(source[1:], target),  # Deletion
        )


"""
Levenshtein Distance

Calculates the Levenshtein distance between two strings.  The Levenshtein distance is defined as the minimum amount of single-character edits (either removing a character, adding a character, or changing a character) necessary to transform a source string into a target string.

Input:
    source: The string you begin with.
    target: The string to transform into.

Output:
    The Levenshtein distance between the source and target.

Example:
    electron can be transformed into neutron by removing the e, turning the l into n, and turning the c into u.
    >>> levenshtein('electron', 'neutron')
    3
"""
