def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)
    # Find the first position where arr[pos] >= x
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    # Check if that position actually contains x
    if lo < len(arr) and arr[lo] == x:
        return lo
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
