def subsequences(a, b, k):
    # Base case: if k is 0, we've successfully formed a subsequence of the desired
    # length (an empty one). To allow for concatenation in the recursive step,
    # we return a list containing an empty list. This ensures that when an
    # element `i` is prepended, it becomes `[i] + [] = [i]`, forming a single-element
    # list for the k=1 case.
    if k == 0:
        return [[]]

    ret = []
    # The loop iterates through possible starting numbers 'i' for the current subsequence.
    # 'a' is the lower bound (inclusive).
    # 'b' is the upper bound (exclusive), as per Python's range(a, b) meaning numbers up to b-1.
    # To form a sequence of length 'k', 'i' must be chosen such that there are
    # at least k-1 numbers remaining after 'i' up to 'b-1'.
    # The largest possible value for 'i' would be (b-1) - (k-1) = b - k.
    # The `range(a, b + 1 - k)` correctly includes numbers from `a` up to `b - k`.
    for i in range(a, b + 1 - k):
        # Recursively find subsequences of length (k-1) starting from 'i + 1'
        # (to ensure ascending order) and staying within the original exclusive
        # upper bound 'b'.
        ret.extend([i] + rest for rest in subsequences(i + 1, b, k - 1))

    return ret


"""
Subsequences


Input:
    a: An int
    b: An int
    k: A positive int

Output:
    A list of all length-k ascending sequences of ints in range(a, b)

Example:
    >>> subsequences(a=1, b=5, k=3)
    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
"""
