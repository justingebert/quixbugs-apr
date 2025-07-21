def longest_common_subsequence(a, b):
    memo = {}

    def _lcs(a, b):
        if not a or not b:
            return ""

        if (a, b) in memo:
            return memo[(a, b)]

        elif a[0] == b[0]:
            result = a[0] + _lcs(a[1:], b[1:])

        else:
            result = max(_lcs(a, b[1:]), _lcs(a[1:], b), key=len)

        memo[(a, b)] = result
        return result

    return _lcs(a, b)


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
