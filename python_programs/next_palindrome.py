def next_palindrome(digit_list):
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2

    # mirror the left side to the right side
    for i in range(low_mid, -1, -1):
        digit_list[len(digit_list) - 1 - i] = digit_list[i]

    # check if the mirrored palindrome is greater than the original
    if digit_list > digit_list:
        return digit_list

    # if not, increment the middle digits and mirror
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2
    carry = 1

    while low_mid >= 0:
        digit_list[low_mid] += carry
        carry = digit_list[low_mid] // 10
        digit_list[low_mid] %= 10
        digit_list[len(digit_list) - 1 - low_mid] = digit_list[low_mid]
        low_mid -= 1

    if carry:
        return [1] + [0] * (len(digit_list) - 1) + [1]
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
