def depth_first_search(startnode, goalnode):
    nodesvisited = set()
    stack = [startnode]

    while stack:
        currentnode = stack.pop()
        if currentnode in nodesvisited:
            continue
        elif currentnode is goalnode:
            return True
        else:
            nodesvisited.add(currentnode)
            for successor in currentnode.successors:
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
