def quicksort(arr):
    if not arr:
        return []

    pivot = arr[len(arr) // 2]  # Use the middle element as the pivot
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
