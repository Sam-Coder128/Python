############################################################################################################################
#
# Program      : Input Conversion Demo
# Input        : 25
# Output       : <class 'str'> , <class 'int'> , <class 'float'> , True
# Description  : Demonstrates how input() always returns a string and how to convert it to other types.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

'''
THEORY:
In Python, the input() function is used to take data from the user.
Regardless of what the user enters, input() always returns the data
as a string (str).

Reason:
input() reads characters typed from the keyboard. Python cannot
automatically determine whether the entered value represents an
integer, float, name, date, or any other type. Therefore, returning
a string is the safest default behavior.

Example:
    If the user enters:
        25

    input() stores it as:
        "25"

which is a string, not an integer.

To use the entered value for mathematical operations, explicit type
conversion is required.

Type Conversion Functions:
1. int()
   Converts a string into an integer.

2. float()
   Converts a string into a floating-point number.

3. bool()
   Converts a value into a Boolean value.
   - Non-empty strings become True
   - Empty strings become False

This process of changing one data type into another is called
type casting or type conversion.
'''

x = input("Enter something: ")

print(type(x))          # <class 'str'> always

# to int
num = int(x)
print(type(num))         # <class 'int'>

# to float
f = float(x)
print(type(f))           # <class 'float'>

# to bool  (non-empty string → True)
b = bool(x)
print(b)                 # True (unless input was empty)

###############################################################################################################################
#
# Application : Shows how to convert string input into int, float, and bool.
#
################################################################################################################################
