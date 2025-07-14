def levenshtein(source, target):
    if source == "" or target == "":
        return len(source) or len(target)

    elif source[0] == target[0]:
        # If the first characters match, there is no cost for this step.
        # The distance is simply the Levenshtein distance of the remaining substrings.
        return levenshtein(source[1:], target[1:])

    else:
        # If the first characters do not match, we consider three operations:
        # 1. Insertion: levenshtein(source, target[1:]) + 1
        # 2. Deletion: levenshtein(source[1:], target) + 1
        # 3. Substitution: levenshtein(source[1:], target[1:]) + 1
        # We take the minimum of these three options. The '+ 1' accounts for the cost
        # of the current operation (insertion, deletion, or substitution).
        return 1 + min(
            levenshtein(source, target[1:]),
            levenshtein(source[1:], target[1:]),
            levenshtein(source[1:], target),
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
