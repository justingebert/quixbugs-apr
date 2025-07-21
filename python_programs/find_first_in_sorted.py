def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1  # hi should be index of last element

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] != x:
                return mid
            else:
                hi = mid - 1  # Continue search in left half
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


"""
Fancy Binary Search
fancy-binsearch


Input:
    arr: A sorted list of ints
    x: A value to find

Output:
    The lowest index i such that arr[i] == x, or -1 if x not in arr

Example:
    >>> find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    2
"""
