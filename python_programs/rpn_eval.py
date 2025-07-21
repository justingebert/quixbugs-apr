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
            # In RPN, the top element popped (a) is the right operand,
            # and the second element popped (b) is the left operand.
            # So the operation should be b OP a.
            a = stack.pop()  # This is the right operand
            b = stack.pop()  # This is the left operand
            stack.append(op(token, b, a))

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
