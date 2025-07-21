import heapq


def shortest_path_length(length_by_edge, startnode, goalnode):
    # distances: dictionary to store the shortest distance found so far from
    # startnode to each node. Initialize startnode's distance to 0, others
    # are implicitly infinity (handled by .get(node, float('inf')))
    distances = {startnode: 0}

    # priority_queue: min-heap storing (distance, tie_breaker, node) tuples,
    # ordered by distance. The tie_breaker is used to ensure comparisons
    # don't fail if node objects are not comparable.
    priority_queue = [(0, 0, startnode)]

    # tie_breaker: A counter to provide a unique element for heap comparisons
    # when distances are equal, preventing TypeError on Node objects.
    tie_breaker = 0

    while priority_queue:
        # Extract the node with the smallest known distance
        current_distance, _, current_node = heapq.heappop(priority_queue)

        # If we have already processed this node with a shorter or equal path,
        # skip this entry. This handles cases where a node is pushed multiple
        # times onto the heap; we only care about the shortest one.
        if current_distance > distances.get(current_node, float("inf")):
            continue

        # If we reached the goal node, return its distance
        if current_node == goalnode:
            return current_distance

        # Iterate over all successor nodes of the current_node
        # Assuming node.successors provides an iterable of successor node objects.
        for nextnode in current_node.successors:
            # Calculate the distance to the nextnode through the current_node
            # Precondition states all lengths are > 0, so no issues with
            # negative cycles.
            # Assuming length_by_edge[(current_node, nextnode)] exists for
            # all successors.
            edge_weight = length_by_edge[(current_node, nextnode)]

            new_path_distance = current_distance + edge_weight

            # If this new path to nextnode is shorter than any previously
            # found path
            if new_path_distance < distances.get(nextnode, float("inf")):
                # Update the shortest distance found for nextnode
                distances[nextnode] = new_path_distance
                # Increment the tie-breaker and add the nextnode to the
                # priority queue with its new shorter distance
                tie_breaker += 1
                heapq.heappush(
                    priority_queue, (new_path_distance, tie_breaker, nextnode)
                )

    # If the loop finishes and goalnode was not reached, it's unreachable
    return float("inf")


"""
Shortest Path

dijkstra

Implements Dijkstra's algorithm for finding a shortest path between two nodes
in a directed graph.

Input:
   length_by_edge: A dict with every directed graph edge's length keyed by its
                   corresponding ordered pair of nodes
   startnode: A node
   goalnode: A node

Precondition:
    all(length > 0 for length in length_by_edge.values())

Output:
    The length of the shortest path from startnode to goalnode in the input
    graph
"""
