def lcs_length(s, t):
    n = len(s)
    m = len(t)

    # dp[i][j] will store the length of the longest common substring
    # ending at s[i-1] and t[j-1].
    # Initialize with zeros.
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0  # To store the maximum length found across all substrings

    # Iterate through strings s and t
    # i and j are 1-based indices for the dp table,
    # corresponding to 0-based indices s[i-1] and t[j-1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match, extend the common substring
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the overall maximum length found
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
            else:
                # If characters do not match, the common substring breaks.
                # So, the length of common substring ending here is 0.
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
