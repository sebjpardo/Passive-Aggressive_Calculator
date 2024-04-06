import math
import string

def getEquationParts(s):
    operators = ['+', '-', '*', '/']

    parts = []  # Result
    currentNumber = ''  # Build up a string of the current number being parsed
    while len(s) > 0:
        char, rest = s[0], s[1:]

        if char in string.digits:
            # Add to current number
            currentNumber += char

        elif char in operators:
            # Push current number to result list
            parts.append(int(currentNumber))

            # Reset current number
            currentNumber = ''

            # Add operator to result
            parts.append(char)

        s = rest

    # Add current number to result
    parts.append(int(currentNumber))

    return parts

print(getEquationParts("1 + 2 - 3 * 4 / 1234"))

#Super Awesome Calculator goes here

def calculate(s):
    listEquation = turnToList(s)
    result = evalEquation(listEquation)
    return result


print(calculate('2 + 2'))

def evalEquation(L):
    length = len(L)
    int1 = L[0]
    operator = L[1]
    if length == 3:
        int2 = L[2]
    if operator == '+':
        return int1 + int2
    elif operator == '-':
        return int1 - int2
    elif operator == '*' or operator == 'x' or operator == 'X':
        return int1 * int2
    elif operator == '/':
        return int1 / int2
    elif operator == '**' or operator == '^':
        return int1 ** int2
    elif operator.lower() == 'sqrt':
        return int1 ** 0.5
    elif operator.lower() == 'sin':
        return math.sin(int1)
    elif operator.lower() == 'cos':
        return math.cos(int1)
    elif operator.lower() == 'tan':
        return math.tan(int1)
    elif operator.lower() == 'abs':
        return abs(int1)