def longest_common_subsequence(a, b):
    if not a or not b:
        return ""

    memo = {}

    def lcs_recursive(s1, s2):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if not s1 or not s2:
            return ""

        elif s1[0] == s2[0]:
            result = s1[0] + lcs_recursive(s1[1:], s2[1:])
        else:
            result = max(lcs_recursive(s1, s2[1:]), lcs_recursive(s1[1:], s2), key=len)
        memo[(s1, s2)] = result
        return result

    return lcs_recursive(a, b)


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
