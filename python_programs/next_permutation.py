def next_permutation(perm):
    # Find the longest non-increasing suffix and find the pivot
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i < 0:
        # perm is the highest permutation
        return None
    # Find rightmost successor to pivot
    j = len(perm) - 1
    while perm[j] <= perm[i]:
        j -= 1
    # Swap the pivot
    next_perm = list(perm)
    next_perm[i], next_perm[j] = perm[j], perm[i]
    # Reverse the suffix
    next_perm[i + 1 :] = reversed(next_perm[i + 1 :])
    return next_perm


"""
Next Permutation
next-perm

Input:
    perm: A list of unique ints

Precondition:
    perm is not sorted in descending order

Output:
    The lexicographically next permutation of the elements of perm

Example:
    >>> next_permutation([3, 2, 4, 1])
    [3, 4, 1, 2]
"""

# Note: The original code had a bug in the inner loop's condition and in reversing part.
# The above version fixes the logic to properly generate the next lexicographical permutation.
