def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}  # Maps a node to its representative set/component

    # Collect all unique nodes from the edges
    all_nodes = set()
    for u, v in weight_by_edge:
        all_nodes.add(u)
        all_nodes.add(v)

    # Initialize each node to be in its own component (a set containing only itself)
    for node in all_nodes:
        group_by_node[node] = {node}

    mst_edges = set()

    # Iterate through edges sorted by weight
    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge

        # Get the component sets for u and v.
        # These are the actual set objects that u and v currently belong to.
        set_u = group_by_node[u]
        set_v = group_by_node[v]

        # If u and v are not in the same component (i.e., they point to different set objects)
        if set_u is not set_v:
            mst_edges.add(edge)

            # Merge the two components.
            # Add all elements of set_v into set_u.
            set_u.update(set_v)

            # All nodes that were previously in set_v's component must now
            # point to the newly merged component (set_u).
            # It's important to iterate over a copy of the elements of set_v
            # because set_v itself is not modified by set_u.update(set_v),
            # but its members' pointers in group_by_node need to be updated.
            # This effectively performs path compression for these nodes.
            for node_in_v_comp in list(set_v):
                group_by_node[node_in_v_comp] = set_u

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
