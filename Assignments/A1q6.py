############################################################################################################################
#
# Program      : Arithmetic Operations Demo
# Input        : Two floating-point numbers
# Output       : Prints results of addition, subtraction, multiplication, and safe division
# Methods      : input(), float(), print(), if-else
# Description  : Demonstrates basic arithmetic operations with safe division handling in Python.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

a = float(input("Enter first number : "))
b = float(input("Enter second number: "))

print("Addition      :", a + b)
print("Subtraction   :", a - b)
print("Multiplication:", a * b)

# Safe division — can't divide by zero
if b != 0:
    print("Division      :", a / b)
else:
    print("Division      : undefined (can't divide by zero)")

###############################################################################################################################
#
# Application : Illustrates how Python performs arithmetic operations and prevents division by zero errors.
#
################################################################################################################################
