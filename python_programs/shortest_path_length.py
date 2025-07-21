from heapq import heappush, heappop
from itertools import count


def shortest_path_length(length_by_edge, startnode, goalnode):
    """
    Dijkstra's algorithm for shortest path length in a directed graph.

    Input:
        length_by_edge: dict mapping (node, node) to positive edge length
        startnode:      start node
        goalnode:       goal node

    Output:
        shortest path length from startnode to goalnode, or
        float('inf') if no path exists.
    """
    # Distance estimates
    dist = {startnode: 0}
    # Min-heap of (distance, counter, node)
    heap = []
    counter = count()
    heappush(heap, (0, next(counter), startnode))
    # Visited nodes
    visited = set()

    while heap:
        current_dist, _, node = heappop(heap)
        if node == goalnode:
            return current_dist
        # Skip entries that are outdated
        if current_dist > dist.get(node, float("inf")):
            continue
        visited.add(node)
        # Relax edges
        for nextnode in node.successors:
            if nextnode in visited:
                continue
            edge_len = length_by_edge.get((node, nextnode))
            if edge_len is None:
                continue
            new_dist = current_dist + edge_len
            if new_dist < dist.get(nextnode, float("inf")):
                dist[nextnode] = new_dist
                heappush(heap, (new_dist, next(counter), nextnode))
    return float("inf")
