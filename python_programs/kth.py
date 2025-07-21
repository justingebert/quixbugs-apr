def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr[1:] if x < pivot]
    above = [x for x in arr[1:] if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above) - 1

    if k < num_less:
        return kth(below, k)
    elif k > num_lessoreq:
        return kth(above, k - num_lessoreq - 1)
    else:
        return pivot


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
