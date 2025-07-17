def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Find all lengths 'j' such that the smallest ending element of an LIS of length 'j'
        # (arr[ends[j]]) is less than the current value 'val'.
        # These are the lengths that 'val' can extend.
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        # Determine the length of the longest LIS that 'val' can extend.
        # If 'val' cannot extend any existing LIS, it starts a new LIS of length 1,
        # so 'length' effectively becomes 0.
        length = max(prefix_lengths) if prefix_lengths else 0

        # The new LIS formed by adding 'val' will have a length of (length + 1).
        new_len = length + 1

        # Update the 'ends' dictionary:
        # 1. If 'new_len' is greater than the current 'longest' known length,
        #    it means we've found a new longest increasing subsequence.
        # 2. Or, if 'new_len' is not greater than 'longest', but 'val' provides a
        #    smaller ending element for an LIS of length 'new_len' than what we currently have.
        #    We use ends.get(new_len, float('inf')) to safely handle cases where ends[new_len]
        #    does not exist yet (i.e., we are setting the first LIS of this length).
        if new_len > longest or val < arr[ends.get(new_len, float("inf"))]:
            ends[new_len] = i
            # Update 'longest' only if a genuinely longer subsequence has been found.
            if new_len > longest:
                longest = new_len

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
