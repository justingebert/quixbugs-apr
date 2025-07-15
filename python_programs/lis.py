def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        # Find all lengths 'j' of existing increasing subsequences
        # such that 'val' can extend them (i.e., val is greater than their ending element).
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        # 'length' is the maximum length of an LIS that 'val' can extend.
        # If prefix_lengths is empty, it means 'val' cannot extend any existing LIS,
        # so it effectively starts a new LIS of length 1. In this case, 'length' is 0.
        length = max(prefix_lengths) if prefix_lengths else 0

        # The new LIS will have length 'length + 1'.
        # We update 'ends[length + 1]' (the index of the smallest ending value for an LIS of this length)
        # if this new LIS is longer than any previously found, or if 'val' provides a smaller
        # ending value for an LIS of this length.
        if length + 1 > longest or val < arr[ends.get(length + 1, float("inf"))]:
            ends[length + 1] = i
            # Update 'longest' if a new maximum length is achieved.
            # This line was the bug: it should use max to ensure 'longest' only increases.
            longest = max(longest, length + 1)

    return longest


"""
Longest Increasing Subsequence
longest-increasing-subsequence


Input:
    arr: A sequence of ints

Precondition:
    The ints in arr are unique

Output:
    The length of the longest monotonically increasing subsequence of arr

Example:
    >>> lis([4, 1, 5, 3, 7, 6, 2])
    3
"""
