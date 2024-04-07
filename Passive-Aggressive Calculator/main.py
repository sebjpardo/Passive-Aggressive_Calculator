from cmu_graphics import *
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

def onAppStart(app):
    app.buttons = [
        ["sin", "cos", "tan", "^"],
        ["abs", "^2", "sqrt", "/"],
        [7, 8, 9, "*"],
        [4, 5, 6, "-"],
        [1, 2, 3, "+"],
        ["<-", 0, "+-", "="]
        ]

def redrawAll(app):
    drawLabel("The Passive Agressive Calculator", 200, 25, size = 20)
    drawCalc(app)

def drawCalc(app):
    drawRect(25, 45, 350, 350, fill = "grey", border = "black", borderWidth = 5)
    drawRect(50, 70, 300, 60, fill = "white", border = "black", borderWidth = 5)
    for row in range(len(app.buttons)):
        for col in range(len(app.buttons[0])):
            x = 50 + col * 80
            y = 150 + row * 40
            button = app.buttons[row][col]
            bColor = "black" if isinstance(button, int) else "white"
            tColor = "white" if isinstance(button, int) else "black"
            drawRect(x, y, 60, 30, fill = bColor)
            drawLabel(str(app.buttons[row][col]), x + 30, y + 15, fill = tColor, size = 16)
