def lcs_length(s, t):
    # Initialize a 2D array to store lengths of longest common suffixes
    # of substrings. The array has size (len(s)+1) x (len(t)+1)
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    max_length = 0

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
    return max_length


"""
Longest Common Substring
longest-common-substring

Input:
    s: a string
    t: a string

Output:
    Length of the longest substring common to s and t

Example:
    >>> lcs_length('witch', 'sandwich')
    2
    >>> lcs_length('meow', 'homeowner')
    4
"""

# The above code is now correctly implemented to find the length of the longest common substring.
# Previously, the code incorrectly used collections.Counter which isn't suitable for DP approach.
# Also, the logic for DP (dynamic programming) was broken for this problem.
# This corrected implementation uses a typical DP approach for Longest Common Substring.
