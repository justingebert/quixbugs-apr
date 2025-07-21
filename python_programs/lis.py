def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        # Find the largest length 'j' such that 'val' can extend a
        # subsequence of length 'j'. This means arr[ends[j]] must be
        # smaller than val.
        # This is equivalent to finding the position where 'val' would be
        # inserted using binary search in a 'tails' array.
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        # 'length' will be the length of the longest LIS that 'val' can extend.
        # If no such LIS exists (val is smaller than all current ends), length is 0.
        length = max(prefix_lengths) if prefix_lengths else 0

        # Case 1: 'val' extends the current longest subsequence.
        # This means length is the current 'longest' (e.g., if longest is 3,
        # and val extends an LIS of length 3, then it forms an LIS of length 4).
        # This is a new maximum length.
        if length == longest:
            ends[length + 1] = i
            longest = length + 1  # Update the overall longest length found so far
        # Case 2: 'val' does not extend the current longest subsequence.
        # This means length < longest. 'val' forms an LIS of length 'length + 1'.
        # We check if 'val' provides a smaller ending element for an existing
        # subsequence length 'length + 1'. If it does, we update 'ends' for that length.
        # This optimization helps future elements extend subsequences.
        elif val < arr[ends[length + 1]]:
            ends[length + 1] = i
            # In this case, 'longest' does not change, as we haven't found
            # a new overall maximum length.
            # The original code incorrectly had 'longest = length + 1' here,
            # which could potentially decrease 'longest' or keep it the same
            # when it should only increase or stay the same in the other branch.

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
