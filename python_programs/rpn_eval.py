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
            # For RPN, the first operand popped (a) is the second argument,
            # and the second operand popped (b) is the first argument.
            a = stack.pop()  # This is the second operand
            b = stack.pop()  # This is the first operand
            stack.append(
                op(token, b, a)  # Call op with (first_operand, second_operand)
            )

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
