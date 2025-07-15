def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == x:
            ans = mid
            hi = mid - 1  # Try to find an earlier occurrence
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return ans


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
