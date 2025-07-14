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
                and opstack[-1] in precedence
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
    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens
