def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        root_u = None
        root_v = None

        # Find the root of the set containing u
        for node in group_by_node:
            if u in group_by_node[node]:
                root_u = node
                break
        if root_u is None:
            group_by_node[u] = {u}
            root_u = u

        # Find the root of the set containing v
        for node in group_by_node:
            if v in group_by_node[node]:
                root_v = node
                break
        if root_v is None:
            group_by_node[v] = {v}
            root_v = v

        if root_u != root_v:
            mst_edges.add(edge)
            # Union the two sets
            group_by_node[root_u].update(group_by_node[root_v])
            # Update all nodes in the merged set to point to the new root
            for node in group_by_node[root_v]:
                group_by_node[node] = group_by_node[root_u]
            # Remove the old root's set to avoid redundancy
            del group_by_node[root_v]

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
