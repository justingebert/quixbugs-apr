from collections import deque


def breadth_first_search(startnode, goalnode):
    """
    Breadth-First Search

    Input:
        startnode: A digraph node
        goalnode: A digraph node

    Output:
        Whether goalnode is reachable from startnode
    """
    queue = deque([startnode])
    nodesseen = {startnode}

    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        for succ in getattr(node, "successors", []):
            if succ not in nodesseen:
                nodesseen.add(succ)
                queue.append(succ)

    return False
