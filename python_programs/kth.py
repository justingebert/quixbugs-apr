def kth(arr, k):
    if not arr:
        return None  # Handle empty array case

    pivot = arr[
        len(arr) // 2
    ]  # Choose median of three or random pivot for better average performance
    below = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = num_less + len(equal)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(
            above, k - num_lessoreq
        )  # Adjust k for the recursive call on 'above'
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
