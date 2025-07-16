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
    seen = {startnode}

    while queue:
        node = queue.popleft()

        if node == goalnode:
            return True

        successors = getattr(node, "successors", [])
        new_nodes = [s for s in successors if s not in seen]
        queue.extend(new_nodes)
        seen.update(new_nodes)

    return False
