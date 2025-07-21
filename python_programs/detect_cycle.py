def detect_cycle(node):
    # Handle cases where the list is empty or has only one node
    if node is None or node.successor is None:
        return False

    # Initialize tortoise (slow pointer) to the head node
    tortoise = node
    # Initialize hare (fast pointer) to two steps ahead of the head
    # If node.successor exists but node.successor.successor does not, hare will be None.
    # The while loop condition will handle this.
    hare = node.successor.successor

    # Loop as long as the hare and its next node are not None.
    # This ensures that hare can always take two steps.
    while hare is not None and hare.successor is not None:
        # Check if the pointers have met
        if hare is tortoise:
            return True

        # Move the pointers
        tortoise = tortoise.successor
        hare = hare.successor.successor

    # If the loop finishes, it means the hare reached the end of the list (None),
    # so there is no cycle.
    return False
