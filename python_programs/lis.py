def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        # Correct the logic of updating ends dictionary:
        # Only update ends[length + 1] if it doesn't exist or val is smaller than the current value at ends[length + 1]
        if length == longest or length + 1 not in ends or val < arr[ends[length + 1]]:
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
