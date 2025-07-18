def lis(arr):
    if not arr:
        return 0

    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        prefix_lengths = [
            j
            for j in range(1, longest + 1)
            if ends.get(j) is not None and arr[ends[j]] < val
        ]
        length = max(prefix_lengths) if prefix_lengths else 0

        if (
            length == longest
            or length + 1 > longest
            or ends.get(length + 1) is None
            or val < arr[ends[length + 1]]
        ):
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
