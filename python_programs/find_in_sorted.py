def find_in_sorted(arr, x):
    def binsearch(start, end):
        # Base case: if the search range is empty (start >= end), x is not found.
        if start >= end:
            return -1

        mid = start + (end - start) // 2

        if x < arr[mid]:
            # x is in the left half, exclusive of mid: [start, mid)
            return binsearch(start, mid)
        elif x > arr[mid]:
            # x is in the right half, exclusive of mid: [mid+1, end)
            # Incrementing mid to mid+1 is crucial to prevent infinite loops
            # when mid == start (e.g., when range is [start, start+1))
            return binsearch(mid + 1, end)
        else:
            # x is found at mid
            return mid

    # Initial call to binsearch covers the entire array: [0, len(arr))
    return binsearch(0, len(arr))
