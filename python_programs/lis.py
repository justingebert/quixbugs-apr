def lis(arr):
    # Use a dictionary to store the index of the minimal tail value of all increasing subsequences of length i+1
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Find the largest j such that arr[ends[j]] < val
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
        length = max(prefix_lengths) if prefix_lengths else 0

        # Insert/update for length+1 subsequence
        if (length + 1) not in ends or val < arr[ends[length + 1]]:
            ends[length + 1] = i

        # Update the longest sequence found so far
        if length + 1 > longest:
            longest = length + 1

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
