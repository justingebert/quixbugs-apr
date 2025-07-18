from heapq import heappush, heappop
import math
import itertools


def shortest_path_length(length_by_edge, startnode, goalnode):
    """
    Implements Dijkstra's algorithm for finding the length
    of the shortest path between two nodes in a directed
    graph.

    Input:
        length_by_edge: A dict mapping each ordered pair
            of nodes to its edge length.
        startnode: A node.
        goalnode: A node.

    Precondition:
        all length_by_edge values are positive.

    Output:
        The length of the shortest path from startnode to
        goalnode, or math.inf if no path exists.
    """
    dist = {startnode: 0}
    visited = set()
    heap = []
    counter = itertools.count()
    heappush(heap, (0, next(counter), startnode))

    while heap:
        distance, _, node = heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == goalnode:
            return distance
        for nextnode in node.successors:
            if nextnode in visited:
                continue
            weight = length_by_edge.get((node, nextnode))
            if weight is None:
                continue
            new_distance = distance + weight
            if new_distance < dist.get(nextnode, math.inf):
                dist[nextnode] = new_distance
                heappush(heap, (new_distance, next(counter), nextnode))
    return math.inf
