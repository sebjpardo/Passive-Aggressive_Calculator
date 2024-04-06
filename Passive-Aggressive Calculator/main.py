import math
import string

#Super Awesome Calculator goes here

def calculate(s):
    listEquation = getEquationParts(s)
    result = evalEquation(listEquation)
    return result

def getEquationParts(s):
    operators = ['+', '-', '*', '/', '**', 'sin', 'cos', 'tan', 'sqrt', 'abs']

    parts = []  # Result
    currentNumber = ''  # Build up a string of the current number being parsed
    currentOperator = '' # Build the operator
    previousTerm = None
    while len(s) > 0:
        char, rest = s[0], s[1:]

        if char.isspace():
            s = rest
            continue

        elif char in string.digits:
            # Add to current number
            currentNumber += char
            if rest == '' or not rest[0].isdigit():
                # Add number to result
                parts.append(int(currentNumber))
                if '-' in currentNumber:
                    previousTerm = currentNumber[1:]
                else:
                    previousTerm = currentNumber

                # Reset current number
                currentNumber = ''

        #elif char in operators:
        else:
            if previousTerm in operators or previousTerm == None:
                if char == '-':
                    currentNumber += char
                    s = rest
                    continue
            
            # Add to current operator
            currentOperator += char

            if rest == '' or rest[0].isdigit() or rest[0].isspace():
                # Add operator to result
                parts.append(currentOperator)
                previousTerm = currentOperator

                # Reset current operator
                currentOperator = ''

        s = rest

    return parts

def evalEquation(L):
    print(L)
    length = len(L)
    if length == 3:
        int1 = L[0]
        operator = L[1]
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
    elif length == 2:
        int1 = L[1]
        operator = L[0]
        if operator.lower() == 'sqrt':
            if int1 < 0:
                return None
            return int1 ** 0.5
        elif operator.lower() == 'sin':
            return math.sin(int1)
        elif operator.lower() == 'cos':
            return math.cos(int1)
        elif operator.lower() == 'tan':
            return math.tan(int1)
        elif operator.lower() == 'abs':
            return abs(int1)
