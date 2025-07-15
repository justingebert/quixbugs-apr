def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        # The bug is in the following line: it incorrectly assigns `longest` to `length`
        # when `length` is 0. This should be `longest = length`.
        # It should be `longest = length + 1` if `length + 1 > longest`
        # and also if `val` is smaller than `arr[ends[length+1]]` and `length + 1` <= `longest`.
        # The correct logic is to find the smallest end element that is greater than val
        # and replace it with val. If no such element exists, then extend the LIS.

        # Find the smallest index `j` such that `arr[ends[j]] >= val`
        l, r = 1, longest
        while l <= r:
            mid = (l + r) // 2
            if arr[ends[mid]] < val:
                l = mid + 1
            else:
                r = mid - 1

        # `l` is the length of the longest increasing subsequence ending with `val`.
        # If `val` is greater than all elements in `ends`, then `l` will be `longest + 1`.
        new_length = l

        # Update `ends` and `longest`.
        ends[new_length] = i
        if new_length > longest:
            longest = new_length

    return longest


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
