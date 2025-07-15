def subsequences(a, b, k):
    if k == 0:
        return [
            []
        ]  # Base case: there is one way to choose 0 elements (the empty sequence).

    ret = []
    # The loop iterates through possible first elements 'i' for the subsequence.
    # The maximum value 'i' can take is such that there are still k-1 elements available
    # after 'i' in the range [i+1, b-1].
    # The last possible element in the overall range is b-1.
    # If we choose 'i' as the first element, and need k-1 more elements,
    # the smallest k-1 elements would be i+1, i+2, ..., i+(k-1).
    # These must be less than or equal to b-1. So, i + (k-1) <= b-1 => i <= b-k.
    # The range function goes up to (end-1), so range(a, b-k+1) is correct for [a, b-k].
    for i in range(a, b + 1 - k):
        # Recursively find subsequences of length k-1 starting from 'i+1' up to 'b-1'.
        # For each such 'rest' subsequence, prepend 'i' to it and add to the results.
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
