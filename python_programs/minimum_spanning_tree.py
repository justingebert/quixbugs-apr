def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        # Ensure both nodes have a group, or initialize group with that node
        if u not in group_by_node:
            group_by_node[u] = {u}
        if v not in group_by_node:
            group_by_node[v] = {v}
        # Only add edge if nodes belong to different groups (to avoid cycle)
        if group_by_node[u] != group_by_node[v]:
            mst_edges.add(edge)
            # Merge groups
            old_group = group_by_node[v]
            new_group = group_by_node[u]
            merged_group = old_group.union(new_group)
            for node in merged_group:
                group_by_node[node] = merged_group

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
