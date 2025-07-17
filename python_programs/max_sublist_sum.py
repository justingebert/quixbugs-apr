def max_sublist_sum(arr):
    # max_ending_here tracks the maximum sum of a sublist ending at the current position.
    # It's reset to 0 if extending the sublist would make its sum negative.
    max_ending_here = 0

    # max_so_far tracks the overall maximum sum found. It's initialized to 0 because
    # an empty sublist has a sum of 0, which is always a potential maximum.
    max_so_far = 0

    for x in arr:
        # Update max_ending_here: either extend the current sublist or start a new one.
        # By taking max(0, ...), we ensure that if the sum becomes negative, it
        # effectively resets to 0, meaning we discard the negative prefix and start fresh.
        max_ending_here = max(0, max_ending_here + x)

        # Update the overall maximum sum found.
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


"""
Max Sublist Sum
max-sublist-sum

Efficient equivalent to max(sum(arr[i:j]) for 0 <= i <= j <= len(arr))

Algorithm based on Kadane's algorithm, adapted to include an empty sublist (sum 0).

Input:
    arr: A list of ints

Output:
    The maximum sublist sum

Example:
    >>> max_sublist_sum([4, -5, 2, 1, -1, 3])
    5
"""
