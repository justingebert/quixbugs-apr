def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1  # Adjusted initial 'hi' to be an inclusive upper bound

    while lo <= hi:
        mid = (lo + hi) // 2

        # Check if arr[mid] is the element we're looking for AND it's the first occurrence.
        # It's the first occurrence if mid is 0 (first element of array)
        # OR if the element before it (arr[mid-1]) is not equal to x.
        if arr[mid] == x and (mid == 0 or x != arr[mid - 1]):
            return mid

        # If x is less than or equal to arr[mid], the first occurrence (if it exists)
        # must be at mid or to its left. So, we search in the left half,
        # excluding mid from the *next* search range since we already checked it.
        elif x <= arr[mid]:
            hi = mid - 1  # Adjusted 'hi' for inclusive upper bound

        # If x is greater than arr[mid], then x must be in the right half.
        else:
            lo = mid + 1

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
