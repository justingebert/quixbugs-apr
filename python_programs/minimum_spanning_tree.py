def find(parent, i):
    # Initialize i as its own parent if not present, otherwise get its current parent.
    # If parent[i] is already i, then i is the root of its set.
    if parent.setdefault(i, i) == i:
        return i
    # Path compression: recursively find the root and set it as parent[i] for faster future lookups.
    parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, i, j):
    # Find the roots (representatives) of the sets containing i and j.
    root_i = find(parent, i)
    root_j = find(parent, j)

    # If the roots are different, it means i and j are in different components.
    # Merge the sets by making one root point to the other.
    if root_i != root_j:
        parent[root_j] = root_i  # Merge j's component under i's component
        return True  # Indicates that a merge occurred
    return False  # Indicates that i and j were already in the same set


def minimum_spanning_tree(weight_by_edge):
    parent = (
        {}
    )  # This dictionary will store the parent of each node, implementing the Union-Find data structure.
    mst_edges = (
        set()
    )  # This set will store the edges that form the Minimum Spanning Tree.

    # Collect all unique nodes from the edges to determine the total number of nodes (N).
    all_nodes = set()
    for u, v in weight_by_edge:
        all_nodes.add(u)
        all_nodes.add(v)
    num_nodes = len(all_nodes)

    # Kruskal's algorithm step 1: Sort all edges in non-decreasing order of their weights.
    # We use .items() to get (edge, weight) pairs and sort by weight.
    sorted_edges = sorted(weight_by_edge.items(), key=lambda item: item[1])

    edges_added = 0
    # A Minimum Spanning Tree for N nodes has exactly N-1 edges if the graph is connected.
    # The problem statement guarantees the input graph is connected.
    target_edges = num_nodes - 1

    # Kruskal's algorithm step 2: Iterate through the sorted edges.
    for (u, v), weight in sorted_edges:
        # Check if adding the current edge (u, v) would form a cycle.
        # This is done by checking if u and v are already in the same connected component.
        # The `union` function returns True if they were in different components (and are now merged),
        # and False if they were already in the same component.
        if union(parent, u, v):
            # If they are in different components, add the edge to the MST.
            mst_edges.add((u, v))
            edges_added += 1
            # Optimization: If we have already added N-1 edges, we have found the MST.
            # No need to process further edges.
            if edges_added == target_edges:
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
