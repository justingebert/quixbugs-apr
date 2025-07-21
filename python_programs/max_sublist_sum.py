def max_sublist_sum(arr):
    if not arr:
        return 0

    max_so_far = arr[0]
    current_max = arr[0]

    for i in range(1, len(arr)):
        x = arr[i]
        current_max = max(x, current_max + x)
        max_so_far = max(max_so_far, current_max)

    # According to the docstring, an empty sublist sum (0) is a valid candidate.
    # If all non-empty sublist sums are negative, 0 should be returned.
    return max(0, max_so_far)


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
