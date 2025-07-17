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
        if isinstance(token, float):
            stack.append(token)
        else:
            # When an operator is encountered, the top two elements are popped.
            # The first pop (a) is the second operand, and the second pop (b) is the first operand.
            # For operations like subtraction and division, the order matters: b OPERATOR a
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(op(token, operand1, operand2))

    return stack.pop()


"""
Reverse Polish Notation

Four-function calculator with input given in Reverse Polish Notation (RPN).

Input:
    A list of values and operators encoded as floats and strings

Precondition:
    all(
        isinstance(token, float) or token in ('+', '-', '*', '/') for token in tokens
    )

Example:
    >>> rpn_eval([3.0, 5.0, '+', 2.0, '/'])
    4.0
"""
