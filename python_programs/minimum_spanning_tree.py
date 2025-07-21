def minimum_spanning_tree(weight_by_edge):
    parent = {}

    def find(u):
        parent.setdefault(u, u)
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        ru = find(u)
        rv = find(v)
        if ru != rv:
            parent[rv] = ru
            return True
        return False

    mst_edges = set()
    for edge in sorted(weight_by_edge, key=weight_by_edge.get):
        u, v = edge
        if union(u, v):
            mst_edges.add(edge)

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
