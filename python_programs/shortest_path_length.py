from heapq import *


def shortest_path_length(length_by_edge, startnode, goalnode):
    unvisited_nodes = []  # FibHeap containing (node, distance) pairs
    heappush(unvisited_nodes, (0, startnode))
    visited_nodes = set()

    while len(unvisited_nodes) > 0:
        distance, node = heappop(unvisited_nodes)
        if node is goalnode:
            return distance

        visited_nodes.add(node)

        for nextnode in get_neighbors(node):
            if nextnode in visited_nodes:
                continue
            new_distance = distance + length_by_edge[(node, nextnode)]

            found = False
            for i, (dist, n) in enumerate(unvisited_nodes):
                if n == nextnode:
                    if new_distance < dist:
                        unvisited_nodes[i] = (new_distance, nextnode)
                        heapify(unvisited_nodes)
                    found = True
                    break
            if not found:
                heappush(unvisited_nodes, (new_distance, nextnode))

    return float("inf")


def get_neighbors(node):
    neighbors = []
    if hasattr(node, "successors"):
        neighbors = node.successors
    return neighbors


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
