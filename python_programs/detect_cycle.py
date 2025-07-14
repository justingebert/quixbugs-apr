def detect_cycle(node):
    # If the list is empty or has only one node, it cannot have a cycle.
    # Also, initialize tortoise and hare to the head node.
    # If the list is empty (node is None), hare and tortoise will be None,
    # and the loop condition will immediately be false, returning False.
    # If it's a single node list, hare.successor will be None, the loop won't run,
    # and it will correctly return False.
    tortoise = node
    hare = node

    # Loop while hare and hare.successor are not None.
    # This ensures that hare can always take two steps.
    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor  # Tortoise moves one step
        hare = hare.successor.successor  # Hare moves two steps

        # If tortoise and hare meet, there is a cycle.
        if hare is tortoise:
            return True

    # If the loop finishes, it means hare reached the end of the list (None),
    # so there is no cycle.
    return False


"""
Linked List Cycle Detection
tortoise-hare

Implements the tortoise-and-hare method of cycle detection.

Input:
    node: The head node of a linked list

Output:
    Whether the linked list is cyclic
"""
