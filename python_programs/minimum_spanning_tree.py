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


def minimum_spanning_tree(weight_by_edge):
    """
    Compute the minimum spanning tree of a connected undirected graph using Kruskal's algorithm.

    Parameters:
        weight_by_edge: dict mapping edge tuples (u, v) to a numeric weight

    Returns:
        A set of edge tuples representing the minimum spanning tree.
    """
    # Union-Find data structures
    parent = {}
    rank = {}

    def find(u):
        # Path compression
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        # Union by rank
        ru = find(u)
        rv = find(v)
        if ru == rv:
            return False
        if rank[ru] < rank[rv]:
            parent[ru] = rv
        else:
            parent[rv] = ru
            if rank[ru] == rank[rv]:
                rank[ru] += 1
        return True

    # Initialize union-find sets
    for u, v in weight_by_edge:
        if u not in parent:
            parent[u] = u
            rank[u] = 0
        if v not in parent:
            parent[v] = v
            rank[v] = 0

    mst_edges = set()
    # Process edges in increasing weight order
    for (u, v), w in sorted(weight_by_edge.items(), key=lambda item: item[1]):
        if union(u, v):
            mst_edges.add((u, v))

    return mst_edges
