def shortest_paths(source, weight_by_edge):
    # Collect all unique nodes from the graph defined by edges
    all_nodes = set()
    for u, v in weight_by_edge.keys():
        all_nodes.add(u)
        all_nodes.add(v)

    # Initialize distances to all nodes to infinity
    weight_by_node = {node: float("inf") for node in all_nodes}

    # Set the source node's distance to 0
    # Ensure source node is included even if it's isolated (not part of any edge tuple)
    if source not in weight_by_node:
        weight_by_node[source] = float("inf")  # Will be immediately overwritten to 0
    weight_by_node[source] = 0

    # The Bellman-Ford algorithm iterates V-1 times, where V is the number of nodes.
    # In each iteration, it relaxes all edges.
    num_nodes = len(weight_by_node)
    for _ in range(num_nodes - 1):
        for (u, v), weight in weight_by_edge.items():
            # Relaxation step: If the path through u to v is shorter than the current path to v
            if (
                weight_by_node[u] != float("inf")
                and weight_by_node[u] + weight < weight_by_node[v]
            ):
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node


"""
Minimum-Weight Paths
bellman-ford

Bellman-Ford algorithm implementation

Given a directed graph that may contain negative edges (as long as there are no negative-weight cycles), efficiently calculates the minimum path weights from a source node to every other node in the graph.

Input:
    source: A node id
    weight_by_edge: A dict containing edge weights keyed by an ordered pair of node ids

Precondition:
    The input graph contains no negative-weight cycles

Output:
   A dict mapping each node id to the minimum weight of a path from the source node to that node

Example:
    >>> shortest_paths('A', {
        ('A', 'B'): 3,
        ('A', 'C'): 3,
        ('A', 'F'): 5,
        ('C', 'B'): -2,
        ('C', 'D'): 7,
        ('C', 'E'): 4,
        ('D', 'E'): -5,
        ('E', 'F'): -1
    })
    {'A': 0, 'C': 3, 'B': 1, 'E': 5, 'D': 10, 'F': 4}
"""
