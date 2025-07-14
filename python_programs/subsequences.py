def subsequences(a, b, k):
    # Base case: If k is 0, there is exactly one subsequence of length 0: the empty list.
    # This is crucial for building longer subsequences by prepending elements.
    if k == 0:
        return [[]]

    ret = []
    # The loop iterates through possible first elements 'i' for a subsequence of length 'k'.
    # 'b' is an exclusive upper bound, meaning numbers from 'a' up to 'b-1' are available.
    # To form a subsequence of length 'k' starting with 'i', there must be 'k-1' elements
    # remaining to be chosen from the range (i+1, b).
    # The largest possible value for 'i' occurs when the last of the 'k' elements is 'b-1'.
    # If 'i' is the first element, and 'k-1' elements follow it, the last element would be at least 'i + (k - 1)'.
    # So, 'i + (k - 1)' must be less than 'b' (or at most 'b-1').
    # This means 'i + k - 1 <= b - 1', which simplifies to 'i <= b - k'.
    # Therefore, 'i' can range from 'a' up to 'b - k' (inclusive).
    # In Python's range function, the end is exclusive, so we use 'b - k + 1'.
    for i in range(a, b - k + 1):
        # Recursively find all subsequences of length 'k-1' starting from 'i + 1'
        # up to the global exclusive upper bound 'b'.
        ret.extend([i] + rest for rest in subsequences(i + 1, b, k - 1))

    return ret


"""
Subsequences


Input:
    a: An int
    b: An int (exclusive upper bound for the numbers in the sequence)
    k: A positive int

Output:
    A list of all length-k ascending sequences of ints in range(a, b)

Example:
    >>> subsequences(a=1, b=5, k=3)
    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
"""
