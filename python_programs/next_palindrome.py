def next_palindrome(digit_list):
    n = len(digit_list)
    res = digit_list[:]
    left = (n - 1) // 2
    right = n // 2

    # Step 1: Mirror left to right
    for i in range(left, -1, -1):
        res[n - i - 1] = res[i]

    # If mirrored number is strictly greater, return it
    if res > digit_list:
        return res

    # Step 2: Increment the center part and mirror again
    carry = 1
    i = left
    j = right
    while i >= 0:
        new_val = res[i] + carry
        carry = new_val // 10
        res[i] = new_val % 10
        res[n - i - 1] = res[i]  # mirror to the corresponding side
        i -= 1

    if carry:
        # all 9's case
        return [1] + [0] * (n - 1) + [1]
    return res


"""
Finds the next palindromic integer when given the current integer
Integers are stored as arrays of base 10 digits from most significant to least significant

Input:
    digit_list: An array representing the current palindrome

Output:
    An array which represents the next palindrome

Preconditions:
    The initial input array represents a palindrome

Example
    >>> next_palindrome([1,4,9,4,1])
    [1,5,0,5,1]
"""
