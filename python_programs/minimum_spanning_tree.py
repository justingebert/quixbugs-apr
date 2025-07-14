def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    def find(node):
        if node not in group_by_node:
            group_by_node[node] = node
            return node
        if group_by_node[node] == node:
            return node
        group_by_node[node] = find(group_by_node[node])
        return group_by_node[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            group_by_node[root1] = root2
            return True
        return False

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
    {(1, 4), (1, 2), (3, 4)}
"""
