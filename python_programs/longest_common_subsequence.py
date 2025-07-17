def longest_common_subsequence(a, b):
    if not a or not b:
        return ""

    elif a[0] == b[0]:
        # If the first characters match, they are part of the LCS.
        # We append this character and recursively find the LCS of the remaining strings.
        return a[0] + longest_common_subsequence(a[1:], b[1:])

    else:
        # If the first characters do not match, we have two possibilities:
        # 1. The LCS does not include a[0]. We find LCS of a[1:] and b.
        # 2. The LCS does not include b[0]. We find LCS of a and b[1:].
        # We take the longer of these two results.
        return max(
            longest_common_subsequence(a, b[1:]),
            longest_common_subsequence(a[1:], b),
            key=len,
        )


"""
Longest Common Subsequence


Calculates the longest subsequence common to the two input strings. (A subsequence is any sequence of letters in the same order
they appear in the string, possibly skipping letters in between.)

Input:
    a: The first string to consider.
    b: The second string to consider.

Output:
    The longest string which is a subsequence of both strings. (If multiple subsequences of equal length exist, either is OK.)

Example:
    >>> longest_common_subsequence('headache', 'pentadactyl')
    'eadac'
"""
