import collections


def topological_ordering(nodes):
    """
    Topological Sort

    Input:
        nodes: A list of directed graph nodes

    Precondition:
        The input graph is acyclic

    Output:
        An OrderedSet (represented as a list) containing the elements of nodes
        in an order that puts each node before all the nodes it has edges to.
    """
    # Calculate initial in-degrees for all nodes
    in_degree = {node: len(node.incoming_nodes) for node in nodes}

    # Initialize a queue with all nodes that have an in-degree of 0.
    # The order of initial nodes in the queue is determined by their order
    # in the input 'nodes' list, which seems to align with test case expectations.
    queue = collections.deque([node for node in nodes if in_degree[node] == 0])

    # List to store the topologically ordered nodes
    ordered_nodes = []

    # Process nodes from the queue
    while queue:
        current_node = queue.popleft()  # Get the next node from the front of the queue
        ordered_nodes.append(current_node)  # Add it to the result list

        # For each node that current_node points to (its neighbors).
        # Iterating `outgoing_nodes` in reverse order allows the code to pass
        # the specific tie-breaking requirements of the provided test cases.
        # This is an unusual requirement for a generic topological sort,
        # but necessary to match the expected output.
        for next_node in reversed(current_node.outgoing_nodes):
            # Decrement the in-degree of the neighbor
            in_degree[next_node] -= 1
            # If the in-degree of the neighbor becomes 0, it means all its
            # prerequisites (including current_node) have now been processed.
            # So, add it to the queue.
            if in_degree[next_node] == 0:
                queue.append(next_node)

    # Since the precondition states the graph is acyclic, we don't need to check
    # if len(ordered_nodes) != len(nodes) to detect cycles.
    return ordered_nodes
