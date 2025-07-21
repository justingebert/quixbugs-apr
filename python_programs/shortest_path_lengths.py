from collections import defaultdict


def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float("inf"))
    # Initialize the diagonal to zero
    for i in range(n):
        length_by_path[i, i] = 0
    # Update with the given edges
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Correct the nested loop to update shortest paths
                new_distance = length_by_path[i, k] + length_by_path[k, j]
                if new_distance < length_by_path[i, j]:
                    length_by_path[i, j] = new_distance

    return length_by_path


"""
All Shortest Paths
floyd-warshall

Floyd-Warshall algorithm implementation.

Calculates the length of the shortest path connecting every ordered pair of nodes in a directed graph.



Input:
    n: The number of nodes in the graph. The nodes are assumed to have ids 0..n-1
    length_by_edge: A dict containing edge length keyed by an ordered pair of node ids

Precondition:
    There are no negative-length cycles in the input graph

Output:
    A dict containing shortest path length keyed by an ordered pair of node ids
"""
