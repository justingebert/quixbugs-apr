def shortest_paths(source, weight_by_edge):
    # Initialize distances for all nodes to infinity
    weight_by_node = {v: float("inf") for u, v in weight_by_edge}
    weight_by_node[source] = 0

    # Relaxation phase: iterate |V| - 1 times
    for _ in range(len(weight_by_node) - 1):
        updated = False
        for (u, v), weight in weight_by_edge.items():
            # Relax the edge: update v's distance if a shorter path is found
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight
                updated = True

        # Early termination if no updates
        if not updated:
            break

    return weight_by_node
