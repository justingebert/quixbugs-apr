def longest_common_subsequence(a, b):
    if not a or not b:
        return ""

    elif a[0] == b[0]:
        # Bug fix: If the first characters match, they are part of the LCS.
        # The remaining LCS is found by comparing the rest of both strings (a[1:] and b[1:]).
        return a[0] + longest_common_subsequence(a[1:], b[1:])

    else:
        return max(
            longest_common_subsequence(a, b[1:]),
            longest_common_subsequence(a[1:], b),
            key=len,
        )
