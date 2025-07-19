def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        # Fix conditions to correctly update ends and longest
        # When length == longest, we should always add a new longer subsequence
        # When val < arr[ends[length + 1]], update ends[length + 1] to a smaller value index
        if length == longest:
            ends[length + 1] = i
            longest = length + 1
        elif (length + 1) in ends:
            if val < arr[ends[length + 1]]:
                ends[length + 1] = i
        else:
            ends[length + 1] = i

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
