def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)
    # Use a half-open interval [lo, hi) to find the first occurrence
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    # After the loop, lo == hi is the insertion point.
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
