def minimum_spanning_tree(weight_by_edge):
    parent = {}
    rank = {}
    mst_edges = set()

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        elif rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i
            rank[root_i] += 1

    # Initialize disjoint sets for each node
    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)

    for node in nodes:
        parent[node] = node
        rank[node] = 0

    # Sort edges by weight
    sorted_edges = sorted(weight_by_edge, key=weight_by_edge.__getitem__)

    # Kruskal's algorithm
    for edge in sorted_edges:
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
