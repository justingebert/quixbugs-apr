def shunting_yard(tokens):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(token)
        elif token in "+-*/":
            while (
                opstack
                and opstack[-1] in "+-*/"
                and precedence[token] <= precedence[opstack[-1]]
            ):
                rpntokens.append(opstack.pop())
            opstack.append(token)
        elif token == "(":
            opstack.append(token)
        elif token == ")":
            while opstack and opstack[-1] != "(":
                rpntokens.append(opstack.pop())
            if opstack and opstack[-1] == "(":
                opstack.pop()
            else:
                raise ValueError("Mismatched parentheses")

    while opstack:
        if opstack[-1] == "(":
            raise ValueError("Mismatched parentheses")
        rpntokens.append(opstack.pop())

    return rpntokens


"""
Infix to RPN Conversion
shunting-yard


Uses Dijkstra's shunting-yard algorithm to transform infix notation into equivalent Reverse Polish Notation.

Input:
    tokens: A list of tokens in infix notation

Precondition:
    all(isinstance(token, int) or token in '+-*/()' for token in tokens)

Output:
    The input tokens reordered into Reverse Polish Notation

Examples:
    >>> shunting_yard([10, '-', 5, '-', 2])
    [10, 5, '-', 2, '-']
    >>> shunting_yard([34, '-', 12, '/', 5])
    [34, 12, 5, '/' ,'-']
    >>> shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    [4, 9, 9, '*', '+', 10, '-', 13, '+']
    >>> shunting_yard([ '(', 3, '+', 4, ')', '*', 5 ])
    [3, 4, '+', 5, '*']
"""
