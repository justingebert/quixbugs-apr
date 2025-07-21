from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)
    nodesseen = set([startnode])

    while queue:
        node = queue.popleft()
        if node is goalnode:
            return True
        for succ in node.successors:
            if succ not in nodesseen:
                nodesseen.add(succ)
                queue.append(succ)

    return False


"""
Breadth-First Search

Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
