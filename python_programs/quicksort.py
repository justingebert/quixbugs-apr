def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = quicksort([x for x in arr if x < pivot])
    equal = [x for x in arr if x == pivot]
    greater = quicksort([x for x in arr if x > pivot])
    return lesser + equal + greater


"""
QuickSort

Input:
    arr: A list of ints

Output:
    The elements of arr in sorted order
"""
