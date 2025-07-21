def next_permutation(perm):
    n = len(perm)
    # Create a mutable copy of the input permutation
    current_perm = list(perm)

    # Step 1: Find the largest index k such that current_perm[k] < current_perm[k + 1]
    # Iterate from right to left
    k = -1
    for i in range(n - 2, -1, -1):
        if current_perm[i] < current_perm[i + 1]:
            k = i
            break

    # According to the precondition "perm is not sorted in reverse order",
    # such a k will always be found. If it were not, this would be the last permutation,
    # and the next would be the first (sorted ascending).

    # Step 2: Find the largest index l > k such that current_perm[k] < current_perm[l]
    # Iterate from right to left, starting from the end of the list down to k+1
    l = -1
    for i in range(n - 1, k, -1):
        if current_perm[k] < current_perm[i]:
            l = i
            break

    # Step 3: Swap current_perm[k] and current_perm[l]
    current_perm[k], current_perm[l] = current_perm[l], current_perm[k]

    # Step 4: Reverse the sub-array current_perm[k + 1:]
    # This part should be reversed in place
    left = k + 1
    right = n - 1
    while left < right:
        current_perm[left], current_perm[right] = (
            current_perm[right],
            current_perm[left],
        )
        left += 1
        right -= 1

    return current_perm


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
