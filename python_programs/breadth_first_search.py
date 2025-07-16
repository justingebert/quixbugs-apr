from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while (
        queue
    ):  # Changed from while True to while queue to handle unreachable goal and empty queue
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # Iterate through successors and add to queue and nodesseen only if truly new
            for successor in node.successors:
                if successor not in nodesseen:
                    nodesseen.add(successor)
                    queue.append(successor)

    return False  # Returns False if the queue becomes empty and goalnode was not found


"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
