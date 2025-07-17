def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)

    for node in nodes:
        group_by_node[node] = {node}

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        group_u = group_by_node[u]
        group_v = group_by_node[v]

        if group_u != group_v:
            mst_edges.add(edge)

            if len(group_u) < len(group_v):
                group_u, group_v = group_v, group_u  # Swap to merge smaller into larger

            group_u.update(group_v)
            for node in group_v:
                group_by_node[node] = group_u

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
