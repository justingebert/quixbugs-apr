import heapq


def shortest_path_length(length_by_edge, startnode, goalnode):
    # Min-heap containing (distance, unique_counter, node) pairs
    unvisited_nodes = []
    counter = 0  # Unique tie-breaker for heap when distances are equal
    heapq.heappush(unvisited_nodes, (0, counter, startnode))
    visited_nodes = set()
    best_distance = {startnode: 0}

    while unvisited_nodes:
        distance, _, node = heapq.heappop(unvisited_nodes)
        if node in visited_nodes:
            continue

        if node == goalnode:
            return distance

        visited_nodes.add(node)

        for nextnode in node.successors:
            if nextnode in visited_nodes:
                continue
            edge = (node, nextnode)
            new_dist = distance + length_by_edge[edge]
            if nextnode not in best_distance or new_dist < best_distance[nextnode]:
                best_distance[nextnode] = new_dist
                counter += 1
                heapq.heappush(unvisited_nodes, (new_dist, counter, nextnode))

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
