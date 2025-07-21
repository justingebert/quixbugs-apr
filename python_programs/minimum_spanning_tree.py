def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        # Ensure ordering is consistent
        if u > v:
            u, v = v, u
        if group_by_node.setdefault(u, {u}) is not group_by_node.setdefault(v, {v}):
            mst_edges.add((u, v))
            # Union the two groups
            group_u = group_by_node[u]
            group_v = group_by_node[v]
            union_group = group_u.union(group_v)
            for node in union_group:
                group_by_node[node] = union_group

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
