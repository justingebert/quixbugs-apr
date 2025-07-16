def lcs_length(s, t):
    """
    Calculates the length of the Longest Common Substring (LCS) between two strings.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        int: The length of the longest common substring.
    """
    s_len = len(s)
    t_len = len(t)

    # Create a 2D DP table initialized with zeros.
    # dp[i][j] will store the length of the longest common substring
    # ending at s[i-1] and t[j-1].
    dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]

    # Variable to keep track of the maximum length found so far
    max_len = 0

    # Fill the DP table
    for i in range(1, s_len + 1):
        for j in range(1, t_len + 1):
            # If characters match, extend the common substring from the diagonal previous cell
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the maximum length found
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
            else:
                # If characters don't match, the common substring is broken,
                # so reset the length for this cell to 0.
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
    >>> lcs_length('abcde', 'ace')
    1
    >>> lcs_length('ababc', 'bab')
    3
    >>> lcs_length('', 'abc')
    0
    >>> lcs_length('abc', '')
    0
    >>> lcs_length('apple', 'banana')
    2
"""
