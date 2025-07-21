def quicksort(arr):
    if not arr:
        return []

    pivot = arr[0]
    # Partition the array into three lists: elements less than the pivot,
    # elements equal to the pivot, and elements greater than the pivot.
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recursively sort the 'less' and 'greater' partitions,
    # then combine them with the 'equal' partition in the middle.
    return quicksort(less) + equal + quicksort(greater)


"""
QuickSort


Input:
    arr: A list of ints

Output:
    The elements of arr in sorted order
"""
