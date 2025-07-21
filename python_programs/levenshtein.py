def levenshtein(source, target):
    if source == "" or target == "":
        return len(source) or len(target)

    elif source[0] == target[0]:
        # If the first characters match, no operation is needed for them.
        # The cost is 0 for this character, so we recurse on the rest of the strings.
        return levenshtein(source[1:], target[1:])

    else:
        # If the first characters do not match, we consider three operations:
        # 1. Insertion: Add target[0] to source (cost 1). Then solve for source and target[1:].
        # 2. Deletion: Remove source[0] from source (cost 1). Then solve for source[1:] and target.
        # 3. Substitution: Change source[0] to target[0] (cost 1). Then solve for source[1:] and target[1:].
        # We take the minimum of these options, plus 1 for the current operation.
        return 1 + min(
            levenshtein(source, target[1:]),  # Insertion (or deletion from target)
            levenshtein(source[1:], target),  # Deletion (or insertion into target)
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
    >>> levenshtein(electron, neutron)
    3
"""
