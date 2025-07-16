def longest_common_subsequence(a, b):
    memo = {}

    def _lcs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(a) or j == len(b):
            return ""

        elif a[i] == b[j]:
            result = a[i] + _lcs(i + 1, j + 1)

        else:
            result = max(_lcs(i, j + 1), _lcs(i + 1, j), key=len)

        memo[(i, j)] = result
        return result

    return _lcs(0, 0)


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
