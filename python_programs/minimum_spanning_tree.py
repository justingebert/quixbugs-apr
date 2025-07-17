def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.get):
        u, v = edge
        if u not in group_by_node:
            group_by_node[u] = {u}
        if v not in group_by_node:
            group_by_node[v] = {v}
        if group_by_node[u] is not group_by_node[v]:
            mst_edges.add(edge)
            # Union: merge the two groups
            combined_group = group_by_node[u].union(group_by_node[v])
            for node in combined_group:
                group_by_node[node] = combined_group

    return mst_edges
