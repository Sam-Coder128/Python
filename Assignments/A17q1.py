############################################################################################################################
#
# Program      : Arithmetic Module Demo
# Input        : 10 5
# Output       : Addition: 15 , Subtraction: 5 , Multiplication: 50 , Division: 2.0
# Description  : Demonstrates module with Add, Sub, Mult, Div functions.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

# Arithmetic.py (module)
def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Mult(a, b):
    return a * b

def Div(a, b):
    return a / b

# main program
import Arithmetic

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", Arithmetic.Add(x, y))
print("Subtraction:", Arithmetic.Sub(x, y))
print("Multiplication:", Arithmetic.Mult(x, y))
print("Division:", Arithmetic.Div(x, y))

###############################################################################################################################
#
# Application : Demonstrates modular programming with arithmetic operations.
#
################################################################################################################################
