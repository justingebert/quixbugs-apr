from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = {startnode}

    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        for successor in node.successors:
            if successor not in nodesseen:
                nodesseen.add(successor)
                queue.append(successor)
    return False


"""
Breadth-First Search

Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
