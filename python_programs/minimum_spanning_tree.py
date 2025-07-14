def minimum_spanning_tree(weight_by_edge):
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
    mst_edges = set()

    # Find all unique nodes
    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)

    # Initialize Disjoint Set Union (DSU) structure
    # Each node is initially its own parent
    parent = {node: node for node in nodes}

    # Find operation with path compression
    def find(node):
        if parent[node] == node:
            return node
        parent[node] = find(parent[node])  # Path compression
        return parent[node]

    # Union operation
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1  # Merge root2's component under root1
            return True  # Components were merged
        return False  # Nodes were already in the same component

    # Kruskal's algorithm
    # Sort edges by weight in ascending order
    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge

        # If adding this edge does not form a cycle (i.e., u and v are in different components)
        if union(u, v):
            mst_edges.add(edge)

        # Optimization: If we have |V|-1 edges, we have found the MST for a connected graph
        if len(mst_edges) == len(nodes) - 1:
            break

    return mst_edges
