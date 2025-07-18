def lcs_length(s, t):
    # Using standard DP for Longest Common Substring
    if not s or not t:
        return 0
    # dp[i][j]: length of longest common substring ending at s[i-1] and t[j-1]
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    ans = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                ans = max(ans, dp[i][j])
    return ans


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
