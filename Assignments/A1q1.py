############################################################################################################################
#
# Program      : Variable Inspection Demo
# Input        : None
# Output       : Prints value, type, memory address, and size of variable
# Methods      : value(), type(), id(), sys.getsizeof()
# Description  : Demonstrates inspecting variables using Python’s built-in functions.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

# value(), type(), id() — the holy trinity for inspecting a variable

x = 42

print("Value   :", x)              # the data stored
print("Type    :", type(x))        # what kind of object it is
print("Address :", id(x))          # memory address (integer)

# bonus: getsizeof tells you how many bytes it takes
import sys
print("Size    :", sys.getsizeof(x), "bytes")

###############################################################################################################################
#
# Application : Shows how to inspect a variable’s value, type, memory address, and size in Python.
#
################################################################################################################################
