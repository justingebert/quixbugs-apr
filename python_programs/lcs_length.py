def lcs_length(s, t):
    m = len(s)
    n = len(t)

    # dp[i][j] stores the length of the longest common substring
    # ending at s[i-1] and t[j-1].
    # Initialize a 2D list with zeros. The extra row/column is for base cases.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_len = 0  # To store the maximum length found anywhere in the dp table

    # Iterate through the strings, using 1-based indexing for the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, extend the common substring
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                # Update max_len if a new maximum is found
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
            else:
                # If characters do not match, the common substring ends here, so reset to 0
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
    1
"""
