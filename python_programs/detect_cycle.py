def detect_cycle(node):
    # Handle empty list or list with a single node (cannot have a cycle)
    if node is None or node.successor is None:
        return False

    tortoise = node
    hare = node

    # The standard Floyd's algorithm ensures hare and tortoise move at least once
    # before checking for equality if they start at the same point.
    # This prevents an immediate false positive if they start at the head and it's a cycle of length 1.
    # However, for a cycle of length 1 (e.g., node -> node), they will meet after one iteration.

    while True:
        # Move tortoise one step
        tortoise = tortoise.successor

        # Move hare two steps, with checks for None at each step
        # This prevents AttributeError if hare.successor or hare.successor.successor is None
        if hare.successor is None:
            return False  # Hare reached the end of the list
        hare = hare.successor

        if hare.successor is None:
            return False  # Hare reached the end of the list on its second step
        hare = hare.successor

        # If hare and tortoise meet, there's a cycle
        if hare is tortoise:
            return True


"""
Linked List Cycle Detection
tortoise-hare

Implements the tortoise-and-hare method of cycle detection.

Input:
    node: The head node of a linked list

Output:
    Whether the linked list is cyclic
"""
