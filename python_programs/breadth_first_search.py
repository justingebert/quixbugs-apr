from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:  # Loop as long as there are nodes to visit
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            for successor_node in node.successors:
                if successor_node not in nodesseen:
                    nodesseen.add(successor_node)  # Mark as seen when adding to queue
                    queue.append(successor_node)

    return False  # Goal node not found after exploring all reachable nodes
