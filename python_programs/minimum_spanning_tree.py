def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        # Initialize groups if not present
        if u not in group_by_node:
            group_by_node[u] = {u}
        if v not in group_by_node:
            group_by_node[v] = {v}

        # If nodes are in different groups, add edge and merge groups
        if group_by_node[u] is not group_by_node[v]:
            mst_edges.add(edge)
            # Merge the two sets
            group_u = group_by_node[u]
            group_v = group_by_node[v]
            # Merge group_v into group_u
            for node in group_v:
                group_node = group_by_node[node]
                # Update all references to point to the merged set
                for n in group_node:
                    group_by_node[n] = group_u
                group_u.update(group_node)

    return mst_edges
