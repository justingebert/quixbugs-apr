def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        # Find the position to place val among existing ends
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        # Update ends if necessary
        if length == longest or val < arr[ends.get(length + 1, -1)]:
            ends[length + 1] = i
            if length + 1 > longest:
                longest = length + 1

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

# Note: The original algorithm had unreliable logic and potential index errors.
# Here's an improved implementation following classic approach:


def lis(arr):
    if not arr:
        return 0
    # tails[i] will hold the last value of the smallest subsequence of length i+1
    tails = []
    for num in arr:
        # Find insertion point
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        # If num is larger than all tails, append it
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    return len(tails)
