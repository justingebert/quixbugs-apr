def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Find the position to insert val in ends to keep ends sorted by values
        # Iterate over existing lengths to find the maximum j where arr[ends[j]] < val
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
        length = max(prefix_lengths) if prefix_lengths else 0
        # Update ends for the next length
        if length + 1 > longest:
            ends[length + 1] = i
            longest = length + 1
        elif length + 1 <= longest:
            # Replace existing value if current index gives a better (smaller) tail
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
