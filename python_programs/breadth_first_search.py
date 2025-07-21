from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    """
    Breadth-First Search

    Input:
        startnode: A digraph node
        goalnode: A digraph node

    Output:
        Whether goalnode is reachable from startnode
    """
    queue = Queue()
    queue.append(startnode)
    nodesseen = set([startnode])

    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        for successor in getattr(node, "successors", []):
            if successor not in nodesseen:
                nodesseen.add(successor)
                queue.append(successor)

    return False
