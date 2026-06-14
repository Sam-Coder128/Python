############################################################################################################################
#
# Program      : Input Type Demo
# Input        : 42
# Output       : <class 'str'> , <class 'int'>
# Description  : Shows that input() returns strings and how to convert them to integers.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

'''

In Python, the input() function is used to accept data from the user.
No matter what value is entered, input() always stores it as a string.

Example:
    If the user enters:
        42

    Python stores it internally as:
        "42"

which belongs to the str data type.

Reason:
input() reads raw keyboard characters and cannot automatically
determine whether the entered value should be treated as an integer,
float, or any other type. Therefore, Python safely returns a string.

To perform mathematical operations, the string must be converted
into an integer using the int() function.

Example:
    int("42")

converts the string "42" into the integer 42.

This process of changing one data type into another is called
type conversion or type casting.
'''

x = input("Enter number: ")
print(type(x))

# OUTPUT: <class 'str'>

# Fix:
x = int(input("Enter number: "))
print(type(x))   # now → <class 'int'>

###############################################################################################################################
#
# Application : Demonstrates that input() returns strings and how to convert them to integers.
#
################################################################################################################################
