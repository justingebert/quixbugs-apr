def lis(arr):
    ends = {}

    for val in arr:
        # Find the smallest key in 'ends' whose value is >= current val using binary search
        l, r = 1, len(ends)
        while l <= r:
            mid = (l + r) // 2
            if mid in ends and arr[ends[mid]] < val:
                l = mid + 1
            else:
                r = mid - 1

        length = l

        if length in ends and val < arr[ends[length]]:
            ends[length] = arr.index(val)  # Optimized to avoid double index operation
        elif length == 1 or val > arr[ends[length - 1]] if length - 1 in ends else True:
            ends[length] = arr.index(val)

    return len(ends)
