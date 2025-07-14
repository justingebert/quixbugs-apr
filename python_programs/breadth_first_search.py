from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    # Handle the edge case where the start node is the goal node
    if startnode is goalnode:
        return True

    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    # Continue as long as there are nodes in the queue to process.
    # The original `while True` would lead to an IndexError if the queue becomes empty
    # and the goalnode is not found, or an infinite loop if the graph has cycles
    # and the goal is unreachable.
    while queue:
        node = queue.popleft()

        # If the current node is the goal, we have found a path
        if node is goalnode:
            return True
        else:
            # Add all successors that have not been seen yet to the queue.
            # This prevents infinite loops in cyclic graphs and redundant processing.
            new_nodes_to_enqueue = [s for s in node.successors if s not in nodesseen]
            queue.extend(new_nodes_to_enqueue)

            # Mark all successors (both new and potentially already seen via another path) as seen.
            # This ensures 'nodesseen' correctly reflects all nodes encountered/processed.
            nodesseen.update(node.successors)

    # If the queue becomes empty and the goalnode was not found, it means
    # the goal is not reachable from the start node.
    return False
