def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        # Make sure we always use (smaller, larger) for undirected edges
        u, v = min(u, v), max(u, v)
        group_by_node.setdefault(u, {u})
        group_by_node.setdefault(v, {v})
        if group_by_node[u] != group_by_node[v]:
            mst_edges.add((u, v))
            combine_set = group_by_node[u] | group_by_node[v]
            for node in combine_set:
                group_by_node[node] = combine_set

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
