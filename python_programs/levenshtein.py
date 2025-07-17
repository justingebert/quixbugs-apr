def levenshtein(source, target):
    # Base cases: if one string is empty, the distance is the length of the other string.
    # This means all characters from the non-empty string must be inserted or deleted.
    if not source:
        return len(target)
    if not target:
        return len(source)

    # If the first characters are the same, no cost is incurred for them.
    # Recurse on the rest of the strings.
    if source[0] == target[0]:
        return levenshtein(source[1:], target[1:])
    # If the first characters are different, consider the minimum of three operations,
    # each incurring a cost of 1:
    # 1. Deletion: Remove the first character from the source string.
    #    (levenshtein(source[1:], target))
    # 2. Insertion: Add the first character from the target string to the source.
    #    (levenshtein(source, target[1:]))
    # 3. Substitution: Change the first character of the source to match the target's.
    #    (levenshtein(source[1:], target[1:]))
    else:
        return 1 + min(
            levenshtein(source[1:], target),  # Deletion
            levenshtein(source, target[1:]),  # Insertion
            levenshtein(source[1:], target[1:]),  # Substitution
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
    >>> levenshtein("electron", "neutron")
    3
"""
