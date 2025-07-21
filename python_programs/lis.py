def lis(arr):
    ends = {0: -1}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [
            j for j in range(0, longest + 1) if arr[ends[j]] < val if ends[j] != -1
        ]
        if -1 in ends and len(prefix_lengths) == 0 and longest == 0:
            prefix_lengths = [0]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or (length + 1 in ends and val < arr[ends[length + 1]]):
            ends[length + 1] = i
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
