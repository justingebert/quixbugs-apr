def lcs_length(s, t):
    m = len(s)
    n = len(t)

    # Create a table to store lengths of longest common suffixes of substrings.
    # dp[i][j] contains length of longest common suffix of s[0..i-1] and t[0..j-1].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # To store the length of the longest common substring
    max_len = 0

    # Fill the dp table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0

    return max_len


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
