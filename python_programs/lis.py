def lis(arr):
    tails = []
    for x in arr:
        if not tails or x > tails[-1]:
            tails.append(x)
        else:
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            tails[l] = x
    return len(tails)


"""
Longest Increasing Subsequence
longest-increasing-subsequence


Input:
    arr: A sequence of ints

Precondition:
    The ints in arr are unique

Output:
    The length of the longest monotonically increasing subsequence of arr

Example:
    >>> lis([4, 1, 5, 3, 7, 6, 2])
    3
"""
