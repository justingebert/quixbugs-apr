from heapq import heappush, heappop


def shortest_path_length(length_by_edge, startnode, goalnode):
    # distances[node] will store the shortest distance found so far from
    # startnode to node. Initialize startnode's distance to 0. Other nodes
    # are implicitly infinity initially.
    distances = {startnode: 0}

    # Priority queue stores (distance, counter, node) tuples. The counter
    # is used as a tie-breaker for nodes with equal distances to ensure
    # that heapq does not try to compare Node objects directly.
    # It automatically retrieves the entry with the smallest distance.
    # The counter ensures uniqueness for comparison.
    priority_queue = [(0, 0, startnode)]
    _counter = 1  # Initialize counter for unique ordering

    # visited_nodes set keeps track of nodes whose shortest path from
    # startnode has been finalized.
    visited_nodes = set()

    while priority_queue:
        # Get the node with the smallest current distance from the priority queue
        current_distance, _, node = heappop(priority_queue)

        # If this node has already been visited, it means we have already
        # processed it with a shorter or equal path, so skip this entry
        # as it's outdated.
        if node in visited_nodes:
            continue

        # If the current node is the goal, we have found the shortest path
        if node == goalnode:
            return current_distance

        # Mark the node as visited, as its shortest path from startnode
        # is now finalized
        visited_nodes.add(node)

        # Explore neighbors of the current node
        # We assume `node` objects have a `successors` attribute which is
        # an iterable of nodes.
        if hasattr(node, "successors"):
            for nextnode in node.successors:
                # Check if there is a direct edge from 'node' to 'nextnode'
                edge_key = (node, nextnode)
                if edge_key not in length_by_edge:
                    continue  # No direct edge defined in length_by_edge

                edge_length = length_by_edge[edge_key]

                # Calculate the distance to the nextnode through the current node
                new_distance = current_distance + edge_length

                # If a shorter path to nextnode is found (or it's the first time
                # we reach it) and nextnode has not been finalized
                # (i.e., not in visited_nodes)
                if nextnode not in distances or new_distance < distances[nextnode]:
                    distances[nextnode] = new_distance
                    # Add (or re-add with a smaller distance) nextnode to the
                    # priority queue. Dijkstra's allows multiple entries for
                    # the same node in the heap; the `visited_nodes` check
                    # handles outdated entries.
                    heappush(priority_queue, (new_distance, _counter, nextnode))
                    _counter += 1

    # If the loop finishes and goalnode was not reached, it's unreachable
    return float("inf")


"""
Shortest Path

dijkstra

Implements Dijkstra's algorithm for finding a shortest path between
two nodes in a directed graph.

Input:
   length_by_edge: A dict with every directed graph edge's length keyed by
                   its corresponding ordered pair of nodes
   startnode: A node
   goalnode: A node

Precondition:
    all(length > 0 for length in length_by_edge.values())

Output:
    The length of the shortest path from startnode to goalnode in the
    input graph
"""
