import math
# Fundamental Functions:
#
#

# aggression = 50 # a number that gets normalized from 0-100 or not

class Equation:
    def __init__(self, parts):
        self.frequency = 1 # gonna need a f'n for this 
        self.parts = parts
        # print(self.get_stress("+"))
        self.stress = self.get_stress(self.parts)

    def __repr__(self):
        if len(self.parts) == 3:
            return f'Parts: {self.parts[0]} {self.parts[1]} {self.parts[2]} | Frequency: {self.frequency} | Stress: {self.stress}'
        if len(self.parts) == 2:
            return f'Parts: operator, {self.parts[1]} constant, {self.parts[0]} | Frequency: {self.frequency} | Stress: {self.stress}'

    def __eq__(self, other):
        if isinstance(other, Equation): # if other of class <<Equation>>, look at each element in self.parts & other.parts
            if len(self.parts) != len(other.parts):
                return False
            for i in range(len(other.parts)):
                if other.parts[i] != self.parts[i]:
                    return False
                    
        elif isinstance(other, list): # if other of type <<list>>, look at each element in self.parts & the list "other"
            if len(self.parts) != len(other):
                return False
            for i in range(len(other)):
                if other[i] != self.parts[i]:
                    return False
        else:
            return False
        
        return True

    #[**, sin, cos, tan, sqrt, abs]
    def get_stress(self, parts):
        if len(parts) > 1:
            sign = parts[1] #always unless there's only one input
        else:
            sign = None
        sign_stress = get_sign_stress(sign)
        
        coeffs = []
        if len(parts) == 3:
            coeffs = [parts[0] + parts[2]]
        elif len(parts) == 2:
            coeffs = [parts[0]]
        elif len(parts) == 1:
            coeffs = [None]
            pass

        numbers_stress = 0
        # stressor_types # a,b,c, and d: correspond to progressively higher numbers
        for coef in coeffs:
            stressor_coeff, stressor_type = get_coeff_stress(coef)
            numbers_stress += stressor_coeff

        return sign_stress + numbers_stress

def get_coeff_stress(integer):
    stressor = 0
    stressor_type = None
    if integer != None:
        integer = int(integer)
        if abs(integer) < 10:
            stressor += 5
            stressor_type == 'a' # a: a 
        elif 10 <= abs(integer) < 100:
            stressor += 1
            stressor_type == 'b'
        elif 100 <= abs(integer) < 10**6:
            stressor += 3
            stressor_type == 'c'
        elif 10**6 <= abs(integer):
                abs_int = abs(integer)
                stressor += 3 * math.log(math.log(abs_int))
                stressor_type == 'd'
    return stressor, stressor_type

def test_coeff_stress():
    c = 5
    assert(get_coeff_stress(c) == 10)
    c = 50
    assert(get_coeff_stress(c) == 2)
    c = 1000
    assert(get_coeff_stress(c) == 4)
    c = 10**9
    print(get_coeff_stress(c))
    # assert(get_coeff_stress(c) == 4)

def get_sign_stress(sign):
    stressor = 0 
    if sign == '+':
        stressor += 5 
    elif sign == '-':
        stressor += 5
    elif sign == "*":
        stressor += 2
    elif sign == "/":
        stressor += 2
    elif sign == "**":
        stressor += 4
    elif sign == "sin":
        stressor += 8
    elif sign == "cos":
        stressor += 8
    elif sign == "tan":
        stressor += 8
    elif sign == "sqrt":
        stressor += 8
    elif sign == None:
        stressor += 9
    return stressor

def test_Equation():
    # test_Equation_eq()   
    test_Equation_stress() 

def test_Equation_eq():
    a = ['0', '+', '1']
    b = ['0', '-', '1']
    c = ['0', '+', '1']

    d = ['4', '']

    eq_a = Equation(a)
    eq_b = Equation(b)
    eq_c = Equation(c)
    print(eq_a)

    print(eq_a, eq_b, eq_c)
    print(eq_a == eq_c, eq_b == eq_c)
    print(eq_a == a, eq_b == b, eq_c == c)

def test_Equation_stress():
    a = ['0', '+', '1']
    b = ['2', '**', '1']
    c = ['0', '+', '1']

    eq_a = Equation(a)
    eq_b = Equation(b)
    eq_c = Equation(c)
    print(eq_a)

    # signs = ['+', '-', '/', 'sin', 'cos', '**']
    # for i in signs:
    #     print(Equation.get_stress(eq_a, i))

def main():
    # test_Equation()
    # test_coeff_stress()
    pass

main()
