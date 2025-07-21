def max_sublist_sum(arr):
    if not arr:
        return 0
    max_ending_here = arr[0]
    max_so_far = arr[0]

    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    # For cases where all numbers are negative, return the maximum element (which max_so_far already holds),
    # but if max_so_far is negative and the problem expects 0 for empty sublist, compare with 0.
    return max_so_far if max_so_far > 0 else 0


"""
Max Sublist Sum
max-sublist-sum

Efficient equivalent to max(sum(arr[i:j]) for 0 <= i <= j <= len(arr))

Algorithm source: WordAligned.org by Thomas Guest


Input:
    arr: A list of ints

Output:
    The maximum sublist sum

Example:
    >>> max_sublist_sum([4, -5, 2, 1, -1, 3])
    5
"""
