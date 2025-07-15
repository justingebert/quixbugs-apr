def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        # Get or create the sets for u and v. These are references to the actual set objects.
        set_u = group_by_node.setdefault(u, {u})
        set_v = group_by_node.setdefault(v, {v})

        # Check if u and v are in different components by comparing the identity of their set objects.
        if set_u is not set_v:
            mst_edges.add(edge)

            # Merge the elements of set_v into set_u.
            # set_u now contains all nodes from both original components.
            # Note: set_v itself is not changed in terms of its object identity,
            # but its contents are effectively now part of set_u.
            set_u.update(set_v)

            # Now, all nodes that were previously pointing to set_v must be updated
            # to point to the newly merged set_u. Iterate over the nodes that were
            # part of set_v's component and update their group_by_node entry.
            # It's safe to iterate directly over set_v, as we only care about its elements (nodes),
            # and it will not be modified during this loop.
            for node in set_v:
                group_by_node[node] = (
                    set_u  # Make the node point to the merged set_u object
                )

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
