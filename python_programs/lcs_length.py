def lcs_length(s, t):
    # Create a 2D dynamic programming table
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    # Maximum length of common substring
    max_length = 0

    # Fill the dp table
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                # If characters match, increment length from previous diagonal
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update max length if needed
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
    2
"""
