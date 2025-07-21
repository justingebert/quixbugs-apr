import heapq
import itertools


def shortest_path_length(length_by_edge, startnode, goalnode):
    # Use a counter to ensure (distance, count, node) is fully comparable in heap,
    # since ties in distance might otherwise attempt to compare Node objects.
    counter = itertools.count()
    unvisited_nodes = []  # Heap containing (distance, count, node) tuples
    heapq.heappush(unvisited_nodes, (0, next(counter), startnode))
    visited_nodes = set()
    dist_by_node = {startnode: 0}

    while unvisited_nodes:
        distance, _, node = heapq.heappop(unvisited_nodes)
        if node == goalnode:
            return distance

        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        for nextnode in node.successors:
            if nextnode in visited_nodes:
                continue
            newdist = distance + length_by_edge[node, nextnode]
            if nextnode not in dist_by_node or newdist < dist_by_node[nextnode]:
                dist_by_node[nextnode] = newdist
                heapq.heappush(unvisited_nodes, (newdist, next(counter), nextnode))

    return float("inf")


"""
Shortest Path

dijkstra

Implements Dijkstra's algorithm for finding a shortest path between two nodes in a directed graph.

Input:
   length_by_edge: A dict with every directed graph edge's length keyed by its corresponding ordered pair of nodes
   startnode: A node
   goalnode: A node

Precondition:
    all(length > 0 for length in length_by_edge.values())

Output:
    The length of the shortest path from startnode to goalnode in the input graph
"""
