def detect_cycle(node):
    # Handle empty list or list with a single node (no cycle possible)
    if node is None or node.successor is None:
        return False

    tortoise = node
    hare = node

    # Move tortoise one step at a time, hare two steps at a time.
    # The loop continues as long as hare and hare.successor are not None,
    # which ensures hare can make two steps.
    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor
        hare = hare.successor.successor

        # If tortoise and hare meet, there is a cycle.
        if tortoise is hare:
            return True

    # If the loop finishes, it means hare reached the end of the list
    # (either hare itself became None or hare.successor became None),
    # without meeting tortoise, indicating no cycle.
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
