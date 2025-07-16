def mergesort(arr):
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:] or right[j:])
        return result

    # The base case for mergesort should be when the array has 0 or 1 elements,
    # as an array with 0 or 1 elements is already considered sorted.
    # The original condition `len(arr) == 0` led to infinite recursion for arrays of length 1.
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)


"""
Merge Sort


Input:
    arr: A list of ints

Output:
    The elements of arr in sorted order
"""
