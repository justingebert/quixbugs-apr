def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1  # Corrected: hi should be the last valid index

    result = -1  # Stores the potential first index found

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == x:
            result = mid  # Found an occurrence, but we need to search left for an earlier one
            hi = mid - 1  # Move to the left half
        elif arr[mid] < x:
            lo = mid + 1  # x is in the right half
        else:  # arr[mid] > x
            hi = mid - 1  # x is in the left half

    return result


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
