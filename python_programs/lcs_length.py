def lcs_length(s, t):
    # Initialize a 2D array to store lengths of longest common suffixes
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    max_length = 0

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
    return max_length
