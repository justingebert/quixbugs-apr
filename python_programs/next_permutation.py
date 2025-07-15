def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    next_perm[i + 1 :] = reversed(next_perm[i + 1 :])
                    return next_perm

    # If no such permutation exists, it means the input is already the lexicographically largest permutation.
    # In this case, we can return the lexicographically smallest permutation (sorted ascending).
    return sorted(perm)


"""
Next Permutation
next-perm


Input:
    perm: A list of unique ints

Precondition:
    perm is not sorted in reverse order (this precondition is now handled by the function)

Output:
    The lexicographically next permutation of the elements of perm

Example:
    >>> next_permutation([3, 2, 4, 1])
    [3, 4, 1, 2]
    >>> next_permutation([1, 2, 3])
    [1, 3, 2]
    >>> next_permutation([3, 2, 1])
    [1, 2, 3]
"""
