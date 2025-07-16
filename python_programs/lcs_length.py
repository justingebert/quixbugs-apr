def lcs_length(s, t):
    # Classic DP for longest common substring
    if not s or not t:
        return 0

    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    maxlen = 0
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            curr = dp[j]
            if s[i - 1] == t[j - 1]:
                dp[j] = prev + 1
                maxlen = max(maxlen, dp[j])
            else:
                dp[j] = 0
            prev = curr
    return maxlen


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
