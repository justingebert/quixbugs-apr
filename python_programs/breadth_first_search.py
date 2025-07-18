from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:  # Fixed: add a termination condition when queue is empty
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # Fix: Only add successors not seen yet
            unvisited_successors = [
                succ for succ in node.successors if succ not in nodesseen
            ]
            queue.extend(unvisited_successors)
            nodesseen.update(unvisited_successors)

    return False


"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
