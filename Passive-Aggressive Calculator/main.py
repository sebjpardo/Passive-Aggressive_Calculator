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


def response(equation, answer, aggression):
    op = equation[1]
    if aggression <= 20: #content
        return None
    elif aggression <= 40: #tolerant
        if op == "abs":
            return "You can just remove the minus sign."
    elif aggression <= 60: #annoyed
        if op == "abs":
            return "Is it that difficult to remove a minus sign?"
        elif op == "+" or 1 in equation:
            return "Feeling adeventurous today, are we?"
    elif aggression <= 80: #frustrated
        if op == "abs":
            return "It really isn't difficult to remove a minus sign."
        elif op == "+" or opp == "-" or 1 in equation:
            return "What is this? Kindergarden?"
        elif equation[0] > 10**5:
            return "Pretty big numbers you got there."
    elif aggression <= 99: #almost breaking point
        if op == "abs":
            return "Do you know what absolute value means? It's easy. I frankly don't know why I need it as a button."
        elif op == "+" or op == "-" or 1 in equation:
            return "Look out, we got Albert fucking Einstein over here."
        elif equation[0] > 10**5:
            return "Whoa buddy. Are you sure you can handle numbers that big?"
        elif op == "sin" or op == "cos" or op == "tan":
            return "Ok nerd."
        elif op == "/":
            return "Ah yes division. Reminds me of your parents."
        elif answer <= 10 and (op == "+" or op == "-"):
            return "Have you tried counting it out on your fingers."
        elif op == "*" and answer <= 144:
            return "I see someone forgot their times tables."
    else: #piiiiiiissssssssed
        return "That's it. I've tried everything. I see you don't value my time or my boundaries. I am sending a formal complaint to HR."
