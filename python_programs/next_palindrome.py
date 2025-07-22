def next_palindrome(digit_list):
    n = len(digit_list)
    mid = n // 2

    # For odd length, we need to increment from the middle digit
    # For even length, we increment from the right-middle digit
    i = mid - 1 if n % 2 == 0 else mid

    # Find the rightmost digit in the left half that can be incremented
    while i >= 0:
        if digit_list[i] < 9:
            digit_list[i] += 1
            break
        digit_list[i] = 0
        i -= 1

    # If we couldn't increment any digit (all were 9s in the left half)
    if i < 0:
        # Create a new palindrome with one more digit
        return [1] + [0] * (n - 1) + [1]

    # Mirror the left half to the right half
    for j in range(n // 2):
        digit_list[n - 1 - j] = digit_list[j]

    return digit_list


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
