############################################################################################################################
#
# Program      : Integer Caching Demo
# Input        : None
# Output       : Prints True/False based on object identity of integers
# Methods      : id(), print()
# Description  : Demonstrates Python’s integer caching mechanism for small integers (-5 to 256).
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

a = 10
b = 10
print(id(a) == id(b))

# OUTPUT: True

# WHY?
# Python keeps a cache of integer objects from -5 to 256.
# When you write a = 10 and b = 10, Python doesn't create
# two separate integer objects.
# Instead, both a and b point to the SAME pre-existing object.
#
# It's like a pantry stocked with labeled boxes.
# "10" already exists — a and b just grab a reference to it.
# Same box → same address → id(a) == id(b) → True
#
# Try it with a = 1000, b = 1000 → you'll get False
# because 1000 is outside the cache range and Python
# creates fresh objects for large integers each time.

###############################################################################################################################
#
# Application : Shows how Python reuses cached small integers, resulting in shared identity for variables with the same value.
#
################################################################################################################################
