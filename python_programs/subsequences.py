def subsequences(a, b, k):
    if k == 0:
        return [[]]  # Corrected: For k=0, there is one subsequence, the empty list.

    ret = []
    # The loop for 'i' goes from 'a' up to 'b - k'.
    # This ensures that there are enough elements remaining after 'i'
    # (i.e., from 'i+1' to 'b-1') to form a subsequence of length 'k-1'.
    # The upper bound 'b + 1 - k' in range() is equivalent to 'b - k' inclusive.
    for i in range(a, b + 1 - k):
        # Recursively find subsequences of length 'k-1'
        # starting from 'i + 1' and still within the original 'b' upper limit.
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
