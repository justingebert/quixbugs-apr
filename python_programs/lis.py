def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Find the length of the longest increasing subsequence ending before 'val'
        # such that its last element is less than 'val'.
        # 'j' represents the length of such a subsequence.
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        # 'length' is the length of the longest LIS that 'val' can extend.
        # If 'prefix_lengths' is empty, it means 'val' cannot extend any existing LIS.
        # In this case, 'val' effectively starts a new LIS of length 1, so 'length' is 0.
        length = max(prefix_lengths) if prefix_lengths else 0

        # The new subsequence ending with 'val' will have length 'length + 1'.
        new_length = length + 1

        # Case 1: We found a new longest increasing subsequence overall.
        # This happens if 'val' extends the previous 'longest' subsequence.
        if new_length > longest:
            ends[new_length] = i
            longest = new_length
        # Case 2: We found an increasing subsequence of 'new_length'
        # whose ending element ('val') is smaller than the currently stored
        # smallest ending element for an LIS of length 'new_length'.
        # A smaller ending element is always preferable as it allows for more future extensions.
        # Note: If new_length <= longest, then new_length is guaranteed to be a key in 'ends'.
        elif val < arr[ends[new_length]]:
            ends[new_length] = i

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
