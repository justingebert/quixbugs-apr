def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        # Mark the current node as visited
        nodesvisited.add(node)

        # If the current node is the goal node, we found it
        if node is goalnode:
            return True

        # Explore neighbors
        for nextnode in node.successors:
            # Only recurse if the neighbor has not been visited yet
            if nextnode not in nodesvisited:
                if search_from(nextnode):
                    return True  # Goal found through this path

        # If no path from this node leads to the goal
        return False

    return search_from(startnode)


"""
Depth-first Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
