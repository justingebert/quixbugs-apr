def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:  # Bug fix: Changed < to >
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = (
                        next_perm[j],
                        next_perm[i],
                    )  # Bug fix: Use next_perm for swap
                    next_perm[i + 1 :] = next_perm[i + 1 :][
                        ::-1
                    ]  # Improved style for reversing slice
                    return next_perm


"""
Next Permutation
next-perm


Input:
    perm: A list of unique ints

Precondition:
    perm is not sorted in reverse order

Output:
    The lexicographically next permutation of the elements of perm

Example:
    >>> next_permutation([3, 2, 4, 1])
    [3, 4, 1, 2]
"""
