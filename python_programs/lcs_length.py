def lcs_length(s, t):
    n = len(s)
    m = len(t)

    # dp[i][j] will store the length of the longest common suffix of s[:i] and t[:j]
    # that ends at s[i-1] and t[j-1].
    # Initialize a 2D list (table) with zeros. Dimensions are (n+1) x (m+1).
    # The first row and column will remain 0, serving as base cases.
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_length = 0

    # Iterate through the strings using 1-based indexing for the dp table
    # i corresponds to s[i-1] and j corresponds to t[j-1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the characters at the current positions match
            if s[i - 1] == t[j - 1]:
                # Extend the common substring from the previous diagonal cell
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the overall maximum length found so far
                max_length = max(max_length, dp[i][j])
            else:
                # If characters do not match, a common substring cannot end here.
                # The length of the common substring ending at this position resets to 0.
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
