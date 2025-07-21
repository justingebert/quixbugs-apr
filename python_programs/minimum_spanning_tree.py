def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    # Helper function to find the representative group of a node
    def find(node):
        # Path compression is not strictly required but useful
        while group_by_node[node] != node:
            group_by_node[node] = group_by_node[group_by_node[node]]
            node = group_by_node[node]
        return node

    # Initialize each node to be its own group
    for edge in weight_by_edge:
        u, v = edge
        for node in (u, v):
            if node not in group_by_node:
                group_by_node[node] = node

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        group_u = find(u)
        group_v = find(v)
        if group_u != group_v:
            mst_edges.add(edge)
            # Union
            group_by_node[group_u] = group_v

    return mst_edges


"""
Minimum Spanning Tree


Kruskal's algorithm implementation.

Input:
    weight_by_edge: A dict of the form {(u, v): weight} for every undirected graph edge {u, v}

Precondition:
    The input graph is connected

Output:
    A set of edges that connects all the vertices of the input graph and has the least possible total weight.

Example:
    >>> minimum_spanning_tree({
    ...     (1, 2): 10,
    ...     (2, 3): 15,
    ...     (3, 4): 10,
    ...     (1, 4): 10
    ... })
    {(1, 2), (3, 4), (1, 4)}
"""
