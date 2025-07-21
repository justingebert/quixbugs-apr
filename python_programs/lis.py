def lis(arr):
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
        4
    """
    tails = (
        []
    )  # tails[i] is the smallest tail of all increasing subsequences of length i+1.
    for num in arr:
        # If we find a tail that is greater or equal than the current number,
        # we replace that tail with the current number because it gives us a better chance
        # to extend the increasing sequence with other numbers that come later.
        if not tails or num > tails[-1]:
            tails.append(num)
        else:
            # Binary search to find the smallest tail >= num
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            tails[l] = num
    return len(tails)
