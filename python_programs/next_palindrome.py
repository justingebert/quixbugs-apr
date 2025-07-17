def next_palindrome(digit_list):
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2

    # Case 1: Mirror and increment the middle digits
    for i in range(low_mid, -1, -1):
        if digit_list[i] < digit_list[len(digit_list) - 1 - i]:
            break
        elif digit_list[i] > digit_list[len(digit_list) - 1 - i]:
            break
    else:
        # The number is the same or smaller, so we need to increment
        for i in range(low_mid, -1, -1):
            if digit_list[i] == 9:
                digit_list[i] = 0
                digit_list[len(digit_list) - 1 - i] = 0
            else:
                digit_list[i] += 1
                digit_list[len(digit_list) - 1 - i] = digit_list[i]
                return digit_list
        return [1] + [0] * (len(digit_list) - 1) + [1]

    # Case 2: Mirror the left side to the right
    for i in range(low_mid + 1):
        digit_list[len(digit_list) - 1 - i] = digit_list[i]
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
