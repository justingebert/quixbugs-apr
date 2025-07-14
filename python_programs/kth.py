def kth(arr, k):
    if not arr:
        return None

    pivot = arr[len(arr) // 2]
    below = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    above = [x for x in arr if x > pivot]

    num_below = len(below)
    num_equal = len(equal)

    if k < num_below:
        return kth(below, k)
    elif k < num_below + num_equal:
        return pivot
    else:
        return kth(above, k - num_below - num_equal)


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
