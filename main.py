from cmu_graphics import *
import math
import string

from Equation import Equation

def test_equation():
    eq_strs = ['4 + 1', '4 / 1', '4 ** 2', 'sin 4', 'sqrt 9', '40 + 1', '40 + 40', 'sqrt 10000']
    for str in eq_strs:
        eq_as_lst = getEquationParts(str)
        eq1 = Equation(eq_as_lst)
        print(eq1)

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

            if rest == '' or rest[0].isdigit() or rest[0].isspace() or rest[0] == '-':
                # Add operator to result
                parts.append(currentOperator)
                previousTerm = currentOperator

                # Reset current operator
                currentOperator = ''

        s = rest
    if len(parts) == 2:
        parts = parts[::-1]
    return parts

def evalEquation(L):
    length = len(L)
    int1 = L[0]
    if not isinstance(int1, int):
        return 0
    if length >= 2:
        operator = L[1]
    if length == 3:
        int2 = L[2]
    if length == 1:
        return int1
    elif operator == '+':
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
    if len(equation) > 1:
        op = equation[1]
    else:
        op = None
    print(equation, answer, aggression)
    if aggression <= 20: #content
        return ""
    elif aggression <= 40: #tolerant
        if op == "abs":
            return "You can just remove the minus sign."
        elif op == None:
            return "Maybe try an actual equation..."
        else:
            "..."
    elif aggression <= 60: #annoyed
        if op == "abs":
            return "Is it that difficult to remove a minus sign?"
        elif op == "+" or 1 in equation:
            return "Feeling adeventurous today, are we?"
        elif answer >= 10**5:
            return "I'm not payed enough for this."
        elif op == None:
            return "Do you know how to use a calculator?"
        else:
            return "..."
    elif aggression <= 80: #frustrated
        if op == "abs":
            return "It really isn't difficult to remove a minus sign."
        elif op == "+" or op == "-" or 1 in equation:
            return "What is this? Kindergarden?"
        elif equation[0] > 10**5:
            return "Pretty big numbers you got there."
        elif answer >= 10**5:
            return "I'm not payed enough for this."
        elif op == None:
            return 'How hard is it to just type an equation!?'
        return "..."
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
        elif answer >= 10**5:
            return "Just big and greedy..."
        elif op == None:
            return "Even a fucking kindergartener can use a calculator! WHy can't you?!?!"
        else:
            return "I'm so done."
    else: #piiiiiiissssssssed
        return "That's it. I've tried everything. I see you don't value my time or my boundaries. I am sending a formal complaint to HR."

def regurgitate():
    return "fuck off and die fuck off and die"

def onAppStart(app):
    app.buttons = [
        ["clr", "abs", "sqrt", "^"],
        ["sin", "cos", "tan", "/"],
        ['7', '8', '9', "*"],
        ['4', '5', '6', "-"],
        ['1', '2', '3', "+"],
        ["<-", '0', "+-", "="]
        ]
    app.buttonsPos = []
    for row in range(len(app.buttons)):
        for col in range(len(app.buttons[0])):
            x = 50 + col * 80
            y = 150 + row * 40
            app.buttonsPos.append((x,y))
    app.pressed_button = None
    app.equation = ''
    app.previousTerm = ''
    app.answer = None
    app.parts = []
    app.previousButton = None
    app.previousKey = None
    
    colors(app)
    za_griDIO(app)
    stress(app)
    app.response = None
    scroll(app)

def stress(app):
    app.stress = 0
    app.equations = dict()

def colors(app):
    app.background_color = "beige"


def za_griDIO(app):
    app.show_grid = False
    app.height = 600
    
    
    rows = 8
    columns = 8
    
    app.col_width = app.width/rows
    app.row_height = app.height/columns
    print(app.col_width, app.row_height)
    app.force_down = app.row_height 

    app.cols = [app.col_width * i for i in range(columns)]
    app.rows = [app.row_height * i for i in range(rows)]

    print(app.rows, app.cols)

def scroll(app):
    app.scroll_steps = 0
    app.scroll_x = 0

    app.scroll_x_increment = 4


def redrawAll(app):
    draw_background(app)
    drawLabel("The Passive Agressive Calculator", 200, 25, size = 20)
    drawCalc(app)
    # A rectangle to block the text that goes off screen
    drawRect(0, 0, 25, app.height, fill = app.background_color) 
    if app.show_grid:
        draw_grid(app)
    if app.stress > 10:
        drawEyes(app)
    
def drawEyes(app):
    drawCircle(30, 80, 20, fill = "white", border = "black", borderWidth = 5)
    drawCircle(370, 80, 20, fill = "white", border = "black", borderWidth = 5)
    drawCircle(30, 80, 10, fill = "black")
    drawCircle(370, 80, 10, fill = "black")
    angle = app.stress / 4
    drawArc(30, 80, 40, 40, 0 - angle, 180, fill = "grey", border = "black", borderWidth = 5)
    drawArc(370, 80, 40, 40, 0 + angle, 180, fill = "grey", border = "black", borderWidth = 5)

def draw_background(app):
    drawRect(0, 0, app.width, app.height, fill = app.background_color)

def drawCalc(app):
    drawRect(25, app.force_down, app.col_width*7, app.row_height*5 + app.row_height/2, fill = "grey", border = "black", borderWidth = 5) # calc background
    drawRect(50, app.force_down+ app.row_height/2, 300, app.row_height + app.row_height/8, fill = "white", border = "black", borderWidth = 5) # this is the display
    for row in range(len(app.buttons)):
        for col in range(len(app.buttons[0])):
            x = 50 + col * 80
            y = 150 + row * 40
            button = app.buttons[row][col]
                
            button_Color = "black" if isinstance(button, int) else "white"

            if button == app.pressed_button:
                button_Color = "slateGray"

            text_Color = "white" if isinstance(button, int) else "black"
            
            drawRect(x, app.force_down + y, 60, 30, fill = button_Color)
            drawLabel(str(app.buttons[row][col]), x + 30, app.force_down + y + 15, fill = text_Color, size = 16)
    

    if app.response != None:
        
        guestimated_average_character_width = 8 + (1/3) 
        font_width = guestimated_average_character_width
        response_length = len(app.response) * font_width
        

        true_x = app.col_width + app.col_width/4
        print(app.scroll_x, response_length)

        draw = True
        if app.scroll_x < response_length:
            true_x = true_x - app.scroll_x
        elif app.scroll_x > response_length:
            draw = False

        if draw:
            drawLabel(app.response, true_x, app.row_height*2 - app.row_height/8, size = 20, align = 'left')

    drawLabel(app.equation, app.col_width + app.col_width/4, app.force_down + 100, size = 20, align = 'left')
    response_mask(app)

def response_mask(app):
    # drawCircle(app.col_width, app.row_height*1.5, 5)  # uncomment these lines to get a clearer idea of
    # drawCircle(app.col_width, app.row_height*2.6, 5)  # what the below code is doing
    drawRect(app.col_width/2, (app.force_down+ app.row_height/2), app.col_width/2, app.row_height + app.row_height/8, fill = 'grey')
    drawRect(app.col_width, (app.force_down+ app.row_height/2), 5, app.row_height + app.row_height/8)
    drawRect(app.col_width/2, app.force_down+ app.row_height/2, 5, app.row_height + app.row_height/8)

def draw_grid(app):
    for x in app.rows:
        drawLine(0, x, app.width, x, fill = 'blue', opacity = 50)
    for y in app.cols:
        drawLine(y, 0, y, app.height, fill = 'blue', opacity = 50)

def fetch_response(app):
    app.response = response(app.parts, app.answer, app.stress)
    print(app.response)

def onMousePress(app, mouseX, mouseY):
    button = getButton(app, mouseX, mouseY)
    app.pressed_button = button                                                 # set app.pressed_button to the button (a string)
    if app.previousButton == '=' or app.previousKey == '=' or app.previousKey == 'enter':
        app.equation = ''
    app.previousKey = None
    if button == '':
        return
    if button == '<-' and app.previousTerm != None:
        app.equation = app.equation[:-len(app.previousTerm)]
    elif button == '+-':
        app.equation = app.equation[:-len(app.previousTerm)]
        if app.equation == '':
            app.previousTerm = '-' + app.previousTerm
        elif app.previousTerm[0] != '-':
            app.previousTerm = '-' + app.previousTerm
        else:
            app.previousTerm = app.previousTerm[1:]
        app.equation += app.previousTerm
    elif button == '=':
        if app.equation != '':
            app.answer = calculate(app.equation)
            app.parts = getEquationParts(app.equation)
            app.equation = calculate(app.equation)
            parts_for_dict = str(app.parts)
            fetch_response(app)
        

            if parts_for_dict in app.equations:
                equation_object = app.equations[parts_for_dict]
                equation_object.frequency += 1

            else:
                app.equations[parts_for_dict] = Equation(app.parts)
                app.stress += app.equations[parts_for_dict].stress

    elif button == 'clr':
        app.equation = ''
    else:
        if not button.isdigit():
            term = button.replace('^', '**')
        else:
            term = button
        app.equation = app.equation + term 
        if term.isdigit() and (app.previousTerm.isdigit() or app.previousTerm == ''):
            print('Hi')
            app.previousTerm += term
        else:
            app.previousTerm = term
    app.previousButton = button

def getButton(app, mX, mY):
    for i in range(len(app.buttonsPos)):
        x, y = app.buttonsPos[i]
        y += app.force_down #dude why the fuck does this work so well
        if x <= mX <= x + 60 and y <= mY <= y + 30:
            return app.buttons[i // 4][i % 4]
    return ''

def onMouseRelease(app, mX, mY):
    app.pressed_button = None

def onKeyPress(app, key):
    if app.previousKey == '=' or app.previousKey == 'enter' or app.previousButton == '=':
        app.equation = ''
    app.previousButton = None
    if key == "g":
        app.show_grid = not app.show_grid
    elif key == '=' or key == 'enter':
        if app.equation != '':
            app.answer = calculate(app.equation)
            app.parts = getEquationParts(app.equation)
            app.equation = calculate(app.equation)
            parts_for_dict = str(app.parts)
            fetch_response(app)
        

            if parts_for_dict in app.equations:
                equation_object = app.equations[parts_for_dict]
                equation_object.frequency += 1

            else:
                app.equations[parts_for_dict] = Equation(app.parts)
                app.stress += app.equations[parts_for_dict].stress
    elif key == 'backspace':
        app.equation = app.equation[:-1]
    elif key == 'space':
        app.equation += ' '
    else:
        app.equation += key
    app.previousKey = key

def onStep(app):
    # print("call")
    scroll_text(app)
    if app.response != None:
        scroll_text(app)

def scroll_text(app):
    app.scroll_steps += 1
    if app.scroll_steps > 30 * 5: #step value times n seconds
        if app.scroll_steps % 20 == 0:
            app.scroll_x += app.scroll_x_increment
            if app.scroll_x > 200:
                app.scroll_x = 0

def main():
    test_equation()
    runApp()

main()