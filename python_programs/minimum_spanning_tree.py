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
    # Collect all unique nodes from the edges
    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)

    # Initialize union-find data structures
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}

    def find(x):
        # Path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # Union by rank
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    # Kruskal's algorithm: sort edges by weight, add if they connect two different components
    mst_edges = set()
    for u, v in sorted(weight_by_edge.keys(), key=lambda e: weight_by_edge[e]):
        if union(u, v):
            mst_edges.add((u, v))

    return mst_edges
