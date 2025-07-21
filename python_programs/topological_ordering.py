def topological_ordering(nodes):
    in_degree = {node: len(node.incoming_nodes) for node in nodes}
    adj = {node: list(node.outgoing_nodes) for node in nodes}
    queue = [node for node in nodes if in_degree[node] == 0]
    ordered = []
    while queue:
        node = queue.pop(0)
        ordered.append(node)
        for succ in reversed(adj.get(node, [])):
            in_degree[succ] -= 1
            if in_degree[succ] == 0:
                queue.append(succ)
    if len(ordered) != len(nodes):
        raise ValueError(
            "Graph contains at least one cycle; " "topological ordering not possible"
        )
    return ordered
