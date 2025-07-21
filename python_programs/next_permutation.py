def next_permutation(perm):
    # Find the largest index i such that perm[i] < perm[i + 1]
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            # Find the largest index j > i such that perm[j] > perm[i]
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:
                    next_perm = list(perm)
                    # Swap perm[i] and perm[j]
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    # Reverse the sequence from perm[i + 1] onwards
                    next_perm[i + 1 :] = reversed(next_perm[i + 1 :])
                    return next_perm
    # If no next permutation, return the permutation as is or handle accordingly
    # Based on the precondition, this case should not occur
    return perm
