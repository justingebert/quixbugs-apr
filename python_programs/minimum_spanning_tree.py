def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    # Use a dict to represent group leaders (disjoint-set by leader)
    leader = {}

    def find(u):
        # Path compression for efficiency
        if leader[u] != u:
            leader[u] = find(leader[u])
        return leader[u]

    def union(u, v):
        leader_u = find(u)
        leader_v = find(v)
        if leader_u != leader_v:
            leader[leader_v] = leader_u
            return True
        return False

    # Set up leader to point to self for all nodes
    for edge in weight_by_edge:
        u, v = edge
        if u not in leader:
            leader[u] = u
        if v not in leader:
            leader[v] = v

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
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
