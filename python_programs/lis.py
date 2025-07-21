def lis(arr):
    # ends[k] stores the index i such that arr[i] is the smallest ending element
    # of an increasing subsequence of length k.
    # This maintains the property: arr[ends[1]] < arr[ends[2]] < ... < arr[ends[longest]].
    ends = {}

    # longest tracks the length of the longest increasing subsequence found so far.
    longest = 0

    for i, val in enumerate(arr):
        # Find the length `j` of the longest increasing subsequence (LIS)
        # that `val` can extend. This means `arr[ends[j]] < val`.
        # `prefix_lengths` will contain all lengths `j` (from 1 to `longest`)
        # for which `arr[ends[j]]` is less than `val`.
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        # `length` is the maximum `j` from `prefix_lengths`. If `prefix_lengths` is empty,
        # `val` cannot extend any existing LIS, so it starts a new LIS of length 1 (meaning `length` is 0).
        length = max(prefix_lengths) if prefix_lengths else 0

        # `new_potential_length` is the length of the LIS that `val` would form.
        # If `val` extends an LIS of length `length`, the new LIS length is `length + 1`.
        new_potential_length = length + 1

        # We need to update `ends[new_potential_length]` and possibly `longest`.
        # There are two cases when `ends[new_potential_length]` should be updated:
        # 1. `new_potential_length` is greater than the current `longest`. This means `val` has formed
        #    a new overall longest increasing subsequence.
        # 2. `new_potential_length` is not greater than `longest`, but `val` provides a smaller
        #    ending element for an existing LIS of length `new_potential_length` than what
        #    is currently stored in `arr[ends[new_potential_length]]`. This helps in finding
        #    even longer subsequences later.

        if new_potential_length > longest:
            # Case 1: We found a new longest increasing subsequence.
            # Update `ends` with the index of `val` for this new longest length.
            ends[new_potential_length] = i
            # Update `longest` to reflect the new maximum length.
            longest = new_potential_length
        elif arr[ends[new_potential_length]] > val:
            # Case 2: `val` can improve an existing LIS of `new_potential_length`
            # by providing a smaller ending element. `longest` does not change.
            ends[new_potential_length] = i
            # `longest` remains unchanged as we are not extending the overall max length,
            # but rather optimizing an existing length's ending value.

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
