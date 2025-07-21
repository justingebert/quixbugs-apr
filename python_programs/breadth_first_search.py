from collections import deque as Queue


def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:  # Loop while the queue is not empty
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            for successor in node.successors:
                if successor not in nodesseen:
                    nodesseen.add(successor)  # Mark node as seen before adding to queue
                    queue.append(successor)

    return False  # If the loop finishes, the goalnode was not found
