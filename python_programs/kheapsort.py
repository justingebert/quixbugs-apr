def kheapsort(arr, k):
    import heapq

    if k <= 0:  # Handle k=0 case separately as heapq.heapify(arr[:0]) is empty
        yield from arr
        return

    heap = arr[:k]
    heapq.heapify(heap)

    for i in range(k, len(arr)):
        yield heapq.heappushpop(heap, arr[i])

    while heap:
        yield heapq.heappop(heap)
