def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Find all lengths `j` such that `arr[ends[j]] < val`.
        # These are the lengths of LIS that `val` can extend.
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        # Determine the potential length of an LIS ending with `val`.
        # If `val` can extend any existing LIS, it extends the longest possible one.
        # So, the new length will be `max(prefix_lengths) + 1`.
        # If `val` cannot extend any existing LIS (e.g., it's smaller than all current ends),
        # it starts a new LIS of length 1.
        if prefix_lengths:
            current_lis_len = max(prefix_lengths) + 1
        else:
            current_lis_len = 1

        # Update `ends[current_lis_len]` if `val` provides a smaller ending
        # element for an LIS of `current_lis_len`, or if `current_lis_len`
        # represents a new maximum length found.
        # The condition `current_lis_len <= longest` handles the case where we
        # are updating an existing length, and we want to ensure `current_lis_len`
        # is a valid key in `ends`.
        if current_lis_len > longest or (
            current_lis_len <= longest and val < arr[ends[current_lis_len]]
        ):
            ends[current_lis_len] = i
            # Update `longest` only if we have found a strictly longer LIS.
            if current_lis_len > longest:
                longest = current_lis_len

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
