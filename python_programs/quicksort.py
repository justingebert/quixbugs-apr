def quicksort(arr):
    if not arr:
        return []

    pivot = arr[len(arr) // 2]  # Changed pivot selection to the middle element
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
