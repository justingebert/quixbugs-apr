from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    nodesseen = set()

    # Add the start node to the queue and mark it as seen
    queue.append(startnode)
    nodesseen.add(startnode)

    # Continue as long as there are nodes to visit in the queue
    while queue:
        node = queue.popleft()

        # If the current node is the goal, we found it
        if node is goalnode:
            return True

        # Explore successors
        for successor in node.successors:
            # If a successor has not been seen before, add it to the queue
            # and mark it as seen to avoid re-processing or cycles.
            if successor not in nodesseen:
                queue.append(successor)
                nodesseen.add(successor)

    # If the queue becomes empty and the goal node was not found, it's unreachable
    return False


"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
