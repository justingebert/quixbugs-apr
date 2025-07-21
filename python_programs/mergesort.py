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
        # extend the remaining elements from left or right
        result.extend(left[i:] or right[j:])
        return result

    # base case: arrays of length 0 or 1 are already sorted
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
