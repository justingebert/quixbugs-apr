def minimum_spanning_tree(weight_by_edge):
    # Initialize each node to be in its own group
    group_by_node = {}
    mst_edges = set()

    # Process edges in order of increasing weight
    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        # Assign default groupings if nodes are new
        group_u = group_by_node.setdefault(u, {u})
        group_v = group_by_node.setdefault(v, {v})

        # If nodes are in different groups, include this edge and merge groups
        if group_u is not group_v:
            mst_edges.add(edge)
            # Merge v's group into u's group
            group_u.update(group_v)
            # Update all nodes in v's group to point to the merged group
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
