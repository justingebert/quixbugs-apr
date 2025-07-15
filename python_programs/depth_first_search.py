def depth_first_search(startnode, goalnode):
    nodesvisited = set()
    path = []

    def search_from(node):
        nonlocal path
        if node in nodesvisited:
            return False
        nodesvisited.add(node)
        path.append(node)
        if node is goalnode:
            return True
        else:
            for nextnode in node.successors:
                if search_from(nextnode):
                    return True
            path.pop()
            return False

    result = search_from(startnode)
    return result


"""
Depth-first Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
