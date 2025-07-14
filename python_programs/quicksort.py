def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(lesser) + equal + quicksort(greater)


"""
QuickSort


Input:
    arr: A list of ints

Output:
    The elements of arr in sorted order
"""
