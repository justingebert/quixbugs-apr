def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # 'length' here represents the length of the longest increasing subsequence
        # that 'val' can extend.
        # This is equivalent to finding the largest 'j' such that arr[ends[j]] < val.
        # If no such 'j' exists, 'length' remains 0.
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
        length = max(prefix_lengths) if prefix_lengths else 0

        # 'potential_new_lis_length' is the length of the LIS that 'val' forms.
        # If 'val' extends an LIS of length 'length', it forms an LIS of length 'length + 1'.
        potential_new_lis_length = length + 1

        # We update the 'ends' dictionary and 'longest' length based on 'val'.
        # There are two main conditions for updating:
        # 1. 'val' creates a new longest increasing subsequence (i.e., its length is greater than current 'longest').
        # 2. 'val' does not create a new longest subsequence, but it provides a
        #    smaller ending element for an LIS of 'potential_new_lis_length'.
        #    A smaller ending element is always preferable as it allows for longer extensions later.

        if potential_new_lis_length > longest:
            # Case 1: This is a new record for the longest increasing subsequence length.
            ends[potential_new_lis_length] = i
            longest = potential_new_lis_length
        elif val < arr[ends[potential_new_lis_length]]:
            # Case 2: 'val' does not extend the overall 'longest' length,
            # but it creates an LIS of 'potential_new_lis_length' that ends with a smaller value.
            # This makes future extensions easier.
            ends[potential_new_lis_length] = i
        # Else: 'val' neither extends the longest LIS nor provides a smaller ending
        # for an existing length, so no update is needed.

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
