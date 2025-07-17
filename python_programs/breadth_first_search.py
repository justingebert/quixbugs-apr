from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while (
        queue
    ):  # Changed from `while True` to `while queue` to correctly handle empty queue
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # Correctly add successors that haven't been seen yet to the queue
            # and update nodesseen with those same successors
            for successor in node.successors:
                if successor not in nodesseen:
                    queue.append(successor)
                    nodesseen.add(successor)

    return False


"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
