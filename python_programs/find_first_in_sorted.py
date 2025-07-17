def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1  # Corrected: 'hi' should be the last valid index, not len(arr)
    result = -1  # Stores the lowest index found so far

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == x:
            # If arr[mid] is x, it's a potential answer.
            # We store it and try to find an even earlier occurrence in the left half.
            result = mid
            hi = mid - 1
        elif arr[mid] < x:
            # If arr[mid] is less than x, x must be in the right half.
            lo = mid + 1
        else:  # arr[mid] > x
            # If arr[mid] is greater than x, x must be in the left half.
            hi = mid - 1

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
