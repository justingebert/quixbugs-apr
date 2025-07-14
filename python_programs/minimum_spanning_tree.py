def minimum_spanning_tree(weight_by_edge):
    parent = {}

    # Collect all unique nodes
    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)

    # Initialize each node to be its own parent
    for node in nodes:
        parent[node] = node

    # Find operation with path compression
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])  # Path compression
        return parent[i]

    # Union operation
    def union(i, j):
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            parent[root_j] = root_i  # Attach root_j's tree to root_i's tree
            return True  # Successfully merged
        return False  # Already in the same set

    mst_edges = set()

    # Sort edges by weight
    sorted_edges = sorted(weight_by_edge.items(), key=lambda item: item[1])

    num_vertices = len(nodes)
    edges_added_count = 0

    for (u, v), weight in sorted_edges:
        if union(u, v):
            mst_edges.add((u, v))
            edges_added_count += 1
            # Optimization: If we have added V-1 edges, we have found the MST
            if edges_added_count == num_vertices - 1:
                break

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
