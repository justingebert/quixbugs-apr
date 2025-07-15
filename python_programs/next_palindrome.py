def next_palindrome(digit_list):
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2

    # Check if the current number is all 9s. If so, return a number of the form 10...01
    all_nines = all(digit == 9 for digit in digit_list)
    if all_nines:
        return [1] + [0] * (len(digit_list) - 1) + [1]

    # Try to increment the higher half of the number, then mirror it
    temp_list = digit_list[:]  # Create a copy
    high_mid = len(temp_list) // 2
    low_mid = (len(temp_list) - 1) // 2

    # Increment the higher half
    while high_mid < len(temp_list):
        if temp_list[low_mid] < temp_list[high_mid]:
            break
        elif temp_list[low_mid] > temp_list[high_mid]:
            break
        elif temp_list[high_mid] == 9:
            temp_list[high_mid] = 0
            temp_list[low_mid] = 0
            high_mid -= 1
            low_mid += 1
        else:
            temp_list[high_mid] += 1
            if low_mid != high_mid:
                temp_list[low_mid] = temp_list[high_mid]
            break

    # Mirror the lower half to the higher
    high_mid = len(temp_list) // 2
    low_mid = (len(temp_list) - 1) // 2
    while low_mid >= 0:
        temp_list[low_mid] = temp_list[high_mid]
        low_mid -= 1
        high_mid += 1

    # If the new number is greater than the original, return it, else increment the high half of the original and mirror again
    if temp_list > digit_list:
        return temp_list

    # Handle the case where incrementing didn't change the number, so we increment from the middle and reflect
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2

    while high_mid < len(digit_list) and low_mid >= 0:
        if digit_list[low_mid] == 9:
            digit_list[low_mid] = 0
            digit_list[high_mid] = 0
        else:
            digit_list[low_mid] += 1
            digit_list[high_mid] = digit_list[low_mid]
            return digit_list

        high_mid += 1
        low_mid -= 1
    return [1] + [0] * (len(digit_list) - 1) + [1]


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
