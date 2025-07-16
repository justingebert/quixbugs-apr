def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # find the length of the longest subsequence ending with a value < val
        if longest > 0:
            prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
            length = max(prefix_lengths) if prefix_lengths else 0
        else:
            length = 0

        new_length = length + 1
        # update the end index for subsequences of length new_length
        if new_length not in ends or val < arr[ends[new_length]]:
            ends[new_length] = i
        # update overall longest if we extended the maximum length
        if new_length > longest:
            longest = new_length

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
