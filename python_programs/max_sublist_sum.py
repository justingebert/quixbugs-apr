def max_sublist_sum(arr):
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        # Update max_ending_here: either extend the current sublist or start a new one (by resetting to 0)
        # If max_ending_here + x becomes negative, it's better to start a new sublist from 0.
        max_ending_here = max(0, max_ending_here + x)
        # Update max_so_far: the maximum sum found globally so far
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


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
