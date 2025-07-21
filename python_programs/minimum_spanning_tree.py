def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge

        # Get the component set for u and v.
        # If a node is new, it starts its own component set.
        comp_u = group_by_node.setdefault(u, {u})
        comp_v = group_by_node.setdefault(v, {v})

        # Check if u and v are already in the same component.
        # They are in the same component if their component sets are the same object.
        if comp_u is not comp_v:
            mst_edges.add(edge)

            # To optimize, merge the smaller component into the larger one.
            # This ensures that comp_u becomes the larger set (or equal size)
            # and will be the target for the merge.
            if len(comp_u) < len(comp_v):
                comp_u, comp_v = comp_v, comp_u

            # Merge comp_v's elements into comp_u.
            # After this, comp_u contains all elements from both original sets.
            # comp_v (the set object itself) remains unchanged.
            comp_u.update(comp_v)

            # Critical step: Update all nodes that were in comp_v
            # to now point to the new merged set (comp_u).
            # This ensures consistency in `group_by_node` lookups.
            for node_in_v_comp in comp_v:
                group_by_node[node_in_v_comp] = comp_u

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
