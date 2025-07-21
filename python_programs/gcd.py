def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two non-negative integers.

    Args:
        a: A non-negative integer.
        b: A non-negative integer.

    Returns:
        The greatest integer that divides evenly into a and b.

    Precondition:
        isinstance(a, int) and isinstance(b, int) and a >= 0 and b >= 0

    Example:
        >>> gcd(35, 21)
        7
        >>> gcd(10, 0)
        10
        >>> gcd(0, 5)
        5
        >>> gcd(0, 0)
        0
    """
    # Ensure non-negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")

    while b:
        a, b = b, a % b
    return a
