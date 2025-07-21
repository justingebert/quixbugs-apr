def lcs_length(s, t):
    n = len(s)
    m = len(t)

    # dp[i][j] stores the length of the longest common substring ending at s[i-1] and t[j-1]
    # We use 1-based indexing for s and t in the DP table for easier handling of base cases.
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                # If characters match, extend the common substring from the previous diagonal element
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the maximum length found so far
                max_len = max(max_len, dp[i][j])
            else:
                # If characters do not match, the common substring is broken,
                # so the length of the common substring ending here is 0.
                # This is already covered by the initialization of dp with zeros.
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
