from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:  # Loop as long as there are nodes in the queue to process
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            for successor in node.successors:
                if successor not in nodesseen:
                    nodesseen.add(successor)  # Mark as seen before adding to queue
                    queue.append(successor)

    return False  # If the queue becomes empty and goalnode was not found


"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
