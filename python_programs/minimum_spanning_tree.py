def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}  # Maps node to its representative set (the set object itself)
    mst_edges = set()

    # Sort edges by weight in ascending order
    sorted_edges = sorted(weight_by_edge, key=weight_by_edge.__getitem__)

    for edge in sorted_edges:
        u, v = edge

        # Get the component set for u. If u is new, create a new set {u}.
        # get_u_group is the actual set object that u belongs to.
        # This acts as the 'find' operation in a Disjoint Set Union (DSU) structure.
        get_u_group = group_by_node.setdefault(u, {u})

        # Get the component set for v.
        get_v_group = group_by_node.setdefault(v, {v})

        # Check if u and v are already in the same component.
        # This is correctly checked by comparing if they point to the *same set object*.
        if get_u_group is not get_v_group:
            # They are in different components, so add the edge to MST
            mst_edges.add(edge)

            # Merge the two components.
            # To optimize, merge the smaller set into the larger one (union by size/rank).
            # The 'target_group' will be the representative set for the merged component.
            if len(get_u_group) >= len(get_v_group):
                target_group = get_u_group
                source_group = get_v_group
            else:
                target_group = get_v_group
                source_group = get_u_group

            # To avoid issues with iterating over a set that is being modified (though
            # source_group itself isn't directly modified by target_group.update(),
            # this makes it robust), create a list of elements from source_group.
            nodes_to_repoint = list(source_group)

            # Perform the set merge: add all elements from source_group into target_group.
            target_group.update(source_group)

            # Update the group_by_node mappings for all nodes that were in the source_group
            # to point to the new, merged target_group. This is crucial for correctness
            # in a DSU implementation where the set object itself represents the component.
            for node in nodes_to_repoint:
                group_by_node[node] = target_group

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
