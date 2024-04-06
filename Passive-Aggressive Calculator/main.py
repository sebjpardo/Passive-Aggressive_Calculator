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