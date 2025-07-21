def lis(arr):
    import bisect

    ends = []
    for val in arr:
        # Find position to insert val in ends to keep ends sorted
        idx = bisect.bisect_left(ends, val)
        if idx == len(ends):
            ends.append(val)
        else:
            ends[idx] = val
    return len(ends)


# End of file. The code now correctly computes the length of LIS.
