############################################################################################################################
#
# Program      : f-string Arithmetic Demo
# Input        : Samruddh 20
# Output       : Hello Samruddh, you will turn 21 next year.
# Description  : Demonstrates inline arithmetic inside f-strings with type conversion.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

'''
An f-string (formatted string literal) is a feature in Python used
to embed variables, expressions, and calculations directly inside
a string.

Syntax:
    f"message {expression}"

Anything written inside {} is evaluated by Python before displaying
the final output.

In this program:
    {age + 1}

performs arithmetic addition directly inside the f-string and inserts
the result into the output string.

The age value must first be converted into an integer using int()
because input() always returns a string.

Example:
    input: "20"

Without conversion:
    "20" + 1

would produce a TypeError because Python cannot add a string and
an integer together.

After conversion:
    20 + 1

Python performs arithmetic addition correctly and produces:
    21

This demonstrates:
1. Type conversion using int()
2. Use of f-strings for formatted output
3. Inline arithmetic expressions inside f-strings
'''

name = input("Enter your name: ")
age  = int(input("Enter your age : "))

# f-string does the math inline
print(f"Hello {name}, you will turn {age + 1} next year.")

###############################################################################################################################
#
# Application : Illustrates how f-strings can embed arithmetic operations directly in formatted output.
#
################################################################################################################################
