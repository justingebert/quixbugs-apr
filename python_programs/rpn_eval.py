def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, (int, float)):  # Allow both integers and floats
            stack.append(float(token))  # Ensure all numbers are floats
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(
                op(
                    token, b, a
                )  # Corrected order of operands for subtraction and division
            )

    return stack.pop()


"""
Reverse Polish Notation

Four-function calculator with input given in Reverse Polish Notation (RPN).

Input:
    A list of values and operators encoded as floats and strings

Precondition:
    all(
        isinstance(token, (int, float)) or token in ('+', '-', '*', '/') for token in tokens
    )

Example:
    >>> rpn_eval([3.0, 5.0, '+', 2.0, '/'])
    4.0
    >>> rpn_eval([5.0, 3.0, '-'])
    2.0
    >>> rpn_eval([3.0, 5.0, '-'])
    -2.0
    >>> rpn_eval([2.0, 3.0, '*', 4.0, '+'])
    10.0
    >>> rpn_eval([10.0, 2.0, '/'])
    5.0
"""
