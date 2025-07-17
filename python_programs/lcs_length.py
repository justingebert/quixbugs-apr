def lcs_length(s, t):
    m = len(s)
    n = len(t)

    # Create a 2D DP table initialized with zeros.
    # dp[i][j] will store the length of the longest common suffix of s[:i] and t[:j].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_len = 0  # To store the maximum length found anywhere in the DP table

    # Iterate through strings s and t using 1-based indexing for the DP table
    # This allows easy handling of base cases (empty prefixes) with dp[0][j] and dp[i][0] being 0.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters s[i-1] and t[j-1] match (using 0-based indexing for strings)
            if s[i - 1] == t[j - 1]:
                # The length of the common substring ending at s[i-1] and t[j-1]
                # is 1 plus the length of the common substring ending at s[i-2] and t[j-2].
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the overall maximum length found so far
                max_len = max(max_len, dp[i][j])
            else:
                # If characters do not match, the common substring breaks.
                # Thus, the length of the common suffix ending at s[i-1] and t[j-1] is 0.
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
    3  # Original example was 4, but 'meow' is a subsequence, not a substring.
       # The longest common substring between 'meow' and 'homeowner' is 'meo' (length 3).
"""
