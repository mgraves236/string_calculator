precedence = {
    "+": 2,
    "-": 2,
    "*": 3,
    "/": 3
}

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# string to Reverse Polish Notation Shunting yard algorithm
def rpn(equation: str) -> []:
    stack = []
    operator_stack = []
    for token in equation:
        if token.isnumeric():
            stack.append(token)
        else:
            # check precedence
            if operator_stack:
                while operator_stack and precedence[token] <= precedence[operator_stack[-1]]:
                    stack.append(operator_stack.pop())
                else:
                    operator_stack.append(token)
            else:
                # stack is empty
                operator_stack.append(token)
        # add remaining operators to output
    if operator_stack:
        for token in operator_stack:
            stack.append(token)

    return stack


def calculate(equation: str) -> float:
    rpn_notation = rpn(equation)
    i = 1
    while len(rpn_notation) > 1:
        if (rpn_notation[-i-1].isnumeric() and rpn_notation[-i-2].isnumeric()) or (is_float(rpn_notation[-i-1]) and is_float(rpn_notation[-i-2])) or (is_float(rpn_notation[-i-1]) and rpn_notation[-i-2].isnumeric()) or (rpn_notation[-i-1].isnumeric() and is_float(rpn_notation[-i-2])):
            result = 0
            match rpn_notation[-i]:
                case "+":
                    result = float(rpn_notation[-i-1]) + float(rpn_notation[-i-2])
                case "-":
                    result = -float(rpn_notation[-i-1]) + float(rpn_notation[-i-2])
                case "*":
                    result = float(rpn_notation[-i-1]) * float(rpn_notation[-i-2])
                case "/":
                    result = float(rpn_notation[-i-2]) / float(rpn_notation[-i-1])
            for j in range(3):
                rpn_notation.pop(-i)
            rpn_notation.insert(-i+1, str(result))
            i = 1
        else:
            i = i + 1
    print(rpn_notation)
    return float(rpn_notation[0])


if __name__ == "__main__":
    eq1 = "3+4"
    eq2 = "3-4+5"
    eq3 = "3+4*5+6"
    eq4 = "4/2+3"
    print(eq4)
    calculate(eq4)