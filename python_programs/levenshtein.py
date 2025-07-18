def levenshtein(source, target):
    if source == "" or target == "":
        # If one string is empty, the distance is the length of the other (all inserts or deletes)
        return len(source) or len(target)

    if source[0] == target[0]:
        # No cost for a match; move on to the rest of the strings
        return levenshtein(source[1:], target[1:])
    else:
        # Cost of 1 for insertion, substitution, or deletion
        return 1 + min(
            levenshtein(source, target[1:]),  # insertion
            levenshtein(source[1:], target[1:]),  # substitution
            levenshtein(source[1:], target),  # deletion
        )


"""
Levenshtein Distance

Calculates the Levenshtein distance between two strings. The Levenshtein distance is defined as the minimum
number of single-character edits (insertions, deletions, or substitutions) required to change one string into
the other.

Input:
    source: The string you begin with.
    target: The string to transform into.

Output:
    The Levenshtein distance between source and target.

Example:
    "electron" can be transformed into "neutron" by removing the 'e', changing 'l' to 'n', and changing 'c' to 'u':
    >>> levenshtein("electron", "neutron")
    3
"""
