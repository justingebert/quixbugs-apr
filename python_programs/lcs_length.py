def lcs_length(s, t):
    m = len(s)
    n = len(t)

    # Create a 2D DP table initialized with zeros
    # dp[i][j] will store the length of the longest common suffix of s[:i] and t[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0  # This will store the maximum length found anywhere in the DP table

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                # If characters match, extend the common substring from the diagonal
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the overall maximum length
                max_length = max(max_length, dp[i][j])
            else:
                # If characters don't match, the common substring breaks, so reset to 0
                dp[i][j] = 0

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
