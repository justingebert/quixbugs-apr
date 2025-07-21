from heapq import heappush, heappop


def shortest_path_length(length_by_edge, startnode, goalnode):
    """
    Dijkstra's algorithm to find the shortest path length from startnode to
    goalnode in a directed graph with positive edge lengths.
    length_by_edge: dict mapping (node, successor) to positive length.
    startnode, goalnode: graph nodes with a .successors list.
    Returns: float distance or float('inf') if unreachable.
    """
    distances = {startnode: 0}
    visited = set()
    # heap entries are (distance, node_id, node) to avoid comparing nodes
    heap = [(0, id(startnode), startnode)]

    while heap:
        dist, _, node = heappop(heap)
        if node in visited:
            continue
        if node == goalnode:
            return dist
        visited.add(node)

        for nextnode in node.successors:
            if nextnode in visited:
                continue
            edge_key = (node, nextnode)
            if edge_key not in length_by_edge:
                continue
            new_dist = dist + length_by_edge[edge_key]
            if new_dist < distances.get(nextnode, float("inf")):
                distances[nextnode] = new_dist
                heappush(heap, (new_dist, id(nextnode), nextnode))

    return float("inf")
