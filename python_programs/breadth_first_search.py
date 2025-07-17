from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # Extend the queue with successors not yet seen
            for successor in node.successors:
                if successor not in nodesseen:
                    queue.append(successor)
            # Mark all the current node's successors as seen
            nodesseen.update(node.successors)

    return False


"""
Breadth-First Search

Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
