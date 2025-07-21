def shortest_paths(source, weight_by_edge):
    # Collect all unique nodes from the graph
    all_nodes = set()
    for u, v in weight_by_edge:
        all_nodes.add(u)
        all_nodes.add(v)
    all_nodes.add(source)  # Ensure the source node is also included, even if isolated

    # Initialize weights for all nodes to infinity, except the source
    weight_by_node = {node: float("inf") for node in all_nodes}
    weight_by_node[source] = 0

    # Get the number of vertices for the loop count (V-1 passes)
    V = len(all_nodes)

    # Relax edges V-1 times
    for i in range(V - 1):
        for (u, v), weight in weight_by_edge.items():
            # Bellman-Ford relaxation step:
            # If the path through u is shorter than the current path to v, update v's weight.
            # This is the corrected line. The original code incorrectly updated weight_by_edge.
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    # The problem states there are no negative-weight cycles,
    # so a final check for negative cycles is not required by the precondition.

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
