def minimum_spanning_tree(weight_by_edge):
    parent = {}

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        parent[find(u)] = find(v)

    # Collect unique nodes and initialize each parent to itself
    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)
    for node in nodes:
        parent[node] = node

    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if find(u) != find(v):
            mst_edges.add(edge)
            union(u, v)

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
