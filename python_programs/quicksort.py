def quicksort(arr):
    if not arr:
        return []

    pivot = arr[0]
    rest = arr[1:]

    lesser = quicksort([x for x in rest if x < pivot])
    equal = [x for x in rest if x == pivot]
    greater = quicksort([x for x in rest if x > pivot])

    return lesser + [pivot] + equal + greater


"""
QuickSort


Input:
    arr: A list of ints

Output:
    The elements of arr in sorted order
"""
