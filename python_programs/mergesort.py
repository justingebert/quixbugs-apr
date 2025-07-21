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
        # Bug was here: result.extend(left[i:] or right[j:])
        # This would only extend one of the left or right if the first was non-empty. It should extend both slices independently.
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:  # also sort arrays of length 1 directly
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
