def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            # Found the pivot at index i
            next_perm = list(perm)  # Create a mutable copy to work on

            # Find the largest index j to the right of i such that next_perm[j] > next_perm[i]
            # Since we iterate from right to left, the first one found will be the correct j.
            for j in range(len(next_perm) - 1, i, -1):
                if (
                    next_perm[j] > next_perm[i]
                ):  # BUG FIX: Changed condition from '<' to '>'
                    # Swap elements at index i and j
                    next_perm[i], next_perm[j] = next_perm[j], next_perm[i]

                    # Reverse the suffix starting from i + 1
                    # This part of the list was in descending order, reversing makes it ascending
                    next_perm[i + 1 :] = next_perm[i + 1 :][
                        ::-1
                    ]  # BUG FIX: More robust way to reverse a slice
                    return next_perm

    # According to the precondition "perm is not sorted in reverse order",
    # this part of the code should not be reached for valid inputs,
    # as a next permutation will always be found and returned within the loop.
    # If the precondition were not guaranteed, this might indicate
    # that 'perm' is the lexicographically largest permutation.
    return perm  # Or raise an error, or return sorted(perm) as the "next" in a cyclic sense.


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
