def next_palindrome(digit_list):
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2

    # Check if the input itself is all 9s
    all_nines = all(digit == 9 for digit in digit_list)
    if all_nines:
        return [1] + [0] * (len(digit_list) - 1) + [1]

    # Increment the left half and mirror
    if digit_list == digit_list[::-1]:  # Handles case where the input is a palindrome

        for i in range(low_mid, -1, -1):
            if digit_list[i] == 9:
                digit_list[i] = 0
            else:
                digit_list[i] += 1
                break
        else:
            digit_list = [1] + [0] * (len(digit_list))

        for i in range(high_mid, len(digit_list)):
            digit_list[i] = digit_list[len(digit_list) - 1 - i]
        return digit_list

    # Copy left side to the right side.
    for i in range(high_mid, len(digit_list)):
        digit_list[i] = digit_list[len(digit_list) - 1 - i]

    if digit_list > digit_list[::-1]:
        return digit_list

    # If after mirroring it, still not a palindrome
    for i in range(low_mid, -1, -1):
        if digit_list[i] == 9:
            digit_list[i] = 0
        else:
            digit_list[i] += 1
            break
    else:
        digit_list = [1] + [0] * (len(digit_list))

    for i in range(high_mid, len(digit_list)):
        digit_list[i] = digit_list[len(digit_list) - 1 - i]

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
