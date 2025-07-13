def lcs_length(s, t):
    n = len(s)
    m = len(t)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    result = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0

    return result


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
