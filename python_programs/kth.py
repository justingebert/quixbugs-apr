def kth(arr, k):
    if not arr:
        return None  # Handle empty array case

    pivot = arr[0]
    below = [x for x in arr[1:] if x < pivot]
    above = [x for x in arr[1:] if x > pivot]
    equal = [x for x in arr[1:] if x == pivot]

    num_less = len(below)
    num_equal = len(equal)

    if k < num_less:
        return kth(below, k)
    elif k < num_less + num_equal + 1:
        return pivot
    else:
        return kth(above, k - num_less - num_equal - 1)


"""
QuickSelect

This is an efficient equivalent to sorted(arr)[k].

Input:
    arr: A list of ints
    k: An int

Precondition:
    0 <= k < len(arr)

Output:
    The kth-lowest element of arr (0-based)
"""
