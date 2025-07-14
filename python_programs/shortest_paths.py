def shortest_paths(source, weight_by_edge):
    weight_by_node = {node: float("inf") for edge in weight_by_edge for node in edge}
    weight_by_node[source] = 0

    num_nodes = len(weight_by_node)
    for i in range(num_nodes - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] != float("inf"):
                weight_by_node[v] = min(weight_by_node[v], weight_by_node[u] + weight)

    return weight_by_node
