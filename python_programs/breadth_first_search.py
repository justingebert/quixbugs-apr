"""
Breadth-First Search

Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""

from collections import deque


def breadth_first_search(startnode, goalnode):
    queue = deque([startnode])
    visited = set([startnode])
    while queue:
        node = queue.popleft()
        if node == goalnode:
            return True
        for succ in node.successors:
            if succ not in visited:
                visited.add(succ)
                queue.append(succ)
    return False
