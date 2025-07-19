def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in ends if j <= longest and arr[ends[j]] < val]

        length = max(prefix_lengths, default=0)

        if length == longest or (length > 0 and val < arr[ends.get(length + 1, i)]):
            ends[length + 1] = i
            longest = max(longest, length + 1)
        elif length == 0 and (longest == 0 or val < arr[ends.get(1, i)]):
            ends[1] = i
            longest = max(longest, 1)

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
