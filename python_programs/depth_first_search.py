def depth_first_search(startnode, goalnode):
    nodesvisited = set()
    stack = [startnode]

    while stack:
        node = stack.pop()
        if node not in nodesvisited:
            if node is goalnode:
                return True
            nodesvisited.add(node)
            for successor in node.successors:
                stack.append(successor)
    return False


"""
Depth-first Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
