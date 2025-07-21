def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # find all lengths j (1..longest) whose current tail is less than val
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
        length = max(prefix_lengths) if prefix_lengths else 0

        # extend the longest subsequence
        if length == longest:
            ends[length + 1] = i
            longest += 1
        # or update a smaller tail for an existing subsequence of length length+1
        elif val < arr[ends[length + 1]]:
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
