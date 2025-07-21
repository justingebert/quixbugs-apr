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

    :param weight_by_edge: dict mapping edge tuple (u, v) to weight.
    :return: set of edges in the minimum spanning tree.
    """
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.get):
        u, v = edge
        set_u = group_by_node.get(u)
        if set_u is None:
            set_u = {u}
        set_v = group_by_node.get(v)
        if set_v is None:
            set_v = {v}
        # if u and v are in different components, include this edge
        if set_u is not set_v:
            mst_edges.add(edge)
            # merge the two components
            merged = set_u.union(set_v)
            # update all nodes in the merged component to point to the new set
            for node in merged:
                group_by_node[node] = merged

    return mst_edges
