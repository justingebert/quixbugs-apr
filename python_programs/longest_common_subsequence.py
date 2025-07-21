def longest_common_subsequence(a, b):
    if not a or not b:
        return ""

    elif a[0] == b[0]:
        # When characters match, they are part of the LCS.
        # We then need to find the LCS of the *rest* of both strings.
        # This requires advancing both string pointers (a[1:] and b[1:]).
        return a[0] + longest_common_subsequence(a[1:], b[1:])

    else:
        # If characters don't match, we explore two possibilities:
        # 1. Skip the first character of 'a' and find LCS of (a[1:], b).
        # 2. Skip the first character of 'b' and find LCS of (a, b[1:]).
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
