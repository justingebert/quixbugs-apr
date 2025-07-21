def quicksort(arr):
    if not arr:
        return []

    pivot = arr[
        len(arr) // 2
    ]  # Changed to median-of-three or middle element for better performance
    lesser = quicksort([x for x in arr if x < pivot])
    equal = [x for x in arr if x == pivot]  # Handling duplicates
    greater = quicksort([x for x in arr if x > pivot])
    return lesser + equal + greater


"""
QuickSort


Input:
    arr: A list of ints

Output:
    The elements of arr in sorted order
"""
