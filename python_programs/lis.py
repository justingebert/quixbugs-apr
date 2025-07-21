def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest:
            # extending the longest subsequence found so far
            ends[length + 1] = i
            longest += 1
        elif val < arr[ends[length + 1]]:
            # better tail candidate for a subsequence of this length
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
