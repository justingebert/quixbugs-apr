def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge

        # Find the representative of the sets containing u and v
        group_u = group_by_node.get(u, {u})
        group_v = group_by_node.get(v, {v})

        if group_u != group_v:
            mst_edges.add(edge)

            # Union the two sets
            new_group = group_u.union(group_v)
            for node in new_group:
                group_by_node[node] = new_group

            # Ensure both u and v are in the group_by_node dictionary
            group_by_node[u] = new_group
            group_by_node[v] = new_group

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
