def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # find all lengths j whose subsequence end is less than val
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
        length = max(prefix_lengths) if prefix_lengths else 0
        new_len = length + 1

        # update the tail index for subsequences of length new_len
        if new_len not in ends or val < arr[ends[new_len]]:
            ends[new_len] = i

        # if we've extended the maximum length, update longest
        if new_len > longest:
            longest = new_len

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
