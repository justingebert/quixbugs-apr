def lcs_length(s, t):
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0

    max_length = 0
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            max_length = max(max_length, dp[i][j])

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
    1
"""
