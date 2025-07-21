from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while (
        queue
    ):  # Fixed bug: Should check if queue is not empty, or else popleft on empty
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # Only enqueue and mark as seen the new unvisited successors
            new_nodes = [succ for succ in node.successors if succ not in nodesseen]
            queue.extend(new_nodes)
            nodesseen.update(new_nodes)

    return False


"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
