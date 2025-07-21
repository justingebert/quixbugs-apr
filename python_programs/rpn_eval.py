"""Reverse Polish Notation

Four-function calculator with input given in Reverse Polish Notation (RPN).

Input:
    A list of values and operators encoded as floats (or ints) and strings

Precondition:
    all(
        isinstance(token, (int, float)) or token in ('+', '-', '*', '/') for token in tokens
    )

Example:
    >>> rpn_eval([3.0, 5.0, '+', 2.0, '/'])
    4.0
"""


def rpn_eval(tokens):
    def op(symbol, a, b):
        if symbol == "+":
            return a + b
        elif symbol == "-":
            return a - b
        elif symbol == "*":
            return a * b
        elif symbol == "/":
            return a / b
        else:
            raise ValueError(f"Unknown operator: {symbol}")

    stack = []
    for token in tokens:
        if isinstance(token, (int, float)):
            stack.append(token)
        elif token in ("+", "-", "*", "/"):
            # In RPN, the first popped is the right operand, second is left
            right = stack.pop()
            left = stack.pop()
            stack.append(op(token, left, right))
        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("The input does not reduce to a single result")
    return stack[0]
