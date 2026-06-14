############################################################################################################################
#
# Program      : Operator Overloading Demo
# Input        : None
# Output       : 1020 , 30
# Description  : Demonstrates Python’s overloaded + operator for strings and integers.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

'''
Python supports operator overloading, which means the same operator
can perform different operations depending on the data types used.

In this program, the + operator behaves differently for strings
and integers.

1. String Concatenation:
   When + is used between strings, Python joins the strings
   together end-to-end.

   Example:
       "10" + "20" = "1020"

   Here, no mathematical addition happens because both operands
   are strings.

2. Integer Addition:
   When + is used between integers, Python performs arithmetic
   addition.

   Example:
       10 + 20 = 30

This demonstrates that Python determines the behavior of operators
based on operand types. This feature is called operator overloading.

Python does not automatically convert strings into integers during
addition. Therefore:
       "10" + 20

produces a TypeError because string and integer types cannot be
directly combined using +.
'''

print("10" + "20")   # OUTPUT: 1020
print(10 + 20)       # OUTPUT: 30

###############################################################################################################################
#
# Application : Shows how Python’s + operator performs concatenation for strings and arithmetic addition for integers.
#
################################################################################################################################
