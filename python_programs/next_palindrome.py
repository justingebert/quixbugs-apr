def next_palindrome(digit_list):
    length = len(digit_list)
    mid_left = (length - 1) // 2
    mid_right = length // 2

    # Function to mirror the left half to the right half
    def mirror_left_to_right():
        for i in range(mid_left + 1):
            digit_list[-(i + 1)] = digit_list[i]

    # Check if current list is a palindrome
    def is_palindrome():
        for i in range(length // 2):
            if digit_list[i] != digit_list[-(i + 1)]:
                return False
        return True

    # Increment the middle part (handles carry over)
    def increment_middle():
        carry = 1
        i = mid_left
        j = mid_right
        while i >= 0:
            new_value = digit_list[i] + carry
            if new_value == 10:
                digit_list[i] = 0
                digit_list[j] = 0
                carry = 1
                i -= 1
                j += 1
            else:
                digit_list[i] = new_value
                if i != j:
                    digit_list[j] = new_value
                carry = 0
                break
        if carry:
            # All digits were 9, so the next palindrome is length+1 with 1's at both ends
            digit_list[:] = [1] + [0] * (length - 1) + [1]

    mirror_left_to_right()
    if digit_list > list(digit_list):
        # Already the next palindrome
        return digit_list
    else:
        # Need to increment the middle and mirror again
        increment_middle()
        mirror_left_to_right()
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
