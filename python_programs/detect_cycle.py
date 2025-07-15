def detect_cycle(node):
    # Handle cases for empty list or list with only one node, no cycle is possible.
    if node is None or node.successor is None:
        return False

    hare = node
    tortoise = node

    # The loop continues indefinitely until a cycle is found or the end of the list is reached.
    while True:
        # Move tortoise one step
        tortoise = tortoise.successor

        # Move hare two steps. We must check for None at each step.
        # If hare's first step leads to None, there's no cycle.
        if hare.successor is None:
            return False
        hare = hare.successor  # Hare moves one step

        # If hare's second step leads to None, there's no cycle.
        if hare.successor is None:
            return False
        hare = hare.successor  # Hare moves the second step

        # Check if hare and tortoise have met.
        # If they meet, a cycle is detected.
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
