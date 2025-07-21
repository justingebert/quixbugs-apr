def next_palindrome(digit_list):
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2

    # Increment the middle digits
    while low_mid >= 0:
        if digit_list[low_mid] == 9:
            digit_list[low_mid] = 0
            if high_mid != low_mid:
                digit_list[high_mid] = 0
            low_mid -= 1
            high_mid += 1
        else:
            digit_list[low_mid] += 1
            if low_mid != high_mid:
                digit_list[high_mid] += 1
            break
    else:
        # If all digits were 9, create a new palindrome like 10...01
        return [1] + [0] * (len(digit_list) - 1) + [1]

    # Ensure the right half mirrors the left half
    left = digit_list[: len(digit_list) // 2]
    right = digit_list[(len(digit_list) + 1) // 2 :]
    right.reverse()

    # If the right half is now lexicographically smaller than the mirrored left half,
    # we need to increment the middle part again and reconstruct.
    # This handles cases like 12921 -> 13031
    if (
        digit_list[(len(digit_list) - 1) // 2] == 0
        and len(digit_list) % 2 == 1
        and digit_list[(len(digit_list) + 1) // 2] == 0
    ):
        # Check if we need to carry over after incrementing middle
        carry = 1
        for i in range(len(digit_list) // 2 - 1, -1, -1):
            if digit_list[i] + carry == 10:
                digit_list[i] = 0
                if (len(digit_list) - 1) // 2 != i:
                    digit_list[len(digit_list) - 1 - i] = 0
            else:
                digit_list[i] += carry
                if (len(digit_list) - 1) // 2 != i:
                    digit_list[len(digit_list) - 1 - i] += carry
                carry = 0
                break
        if carry:
            return [1] + [0] * (len(digit_list) - 1) + [1]

    for i in range(len(digit_list) // 2):
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
