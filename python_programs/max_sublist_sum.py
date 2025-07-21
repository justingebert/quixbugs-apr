def max_sublist_sum(arr):
    """
    Max Sublist Sum
    max-sublist-sum

    Efficient equivalent to max(sum(arr[i:j]) for 0 <= i <= j <= len(arr))

    Algorithm source: WordAligned.org by Thomas Guest

    Input:
        arr: A list of ints

    Output:
        The maximum sublist sum (or 0 if all are negative or list is empty)

    Examples:
        >>> max_sublist_sum([4, -5, 2, 1, -1, 3])
        5
        >>> max_sublist_sum([-3, -2, -5])
        0
        >>> max_sublist_sum([])
        0
    """
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        # reset running sum to zero if it goes negative,
        # so we only accumulate positive contributions
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
