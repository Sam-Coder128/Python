############################################################################################################################
#
# Program      : Object Identity Demo
# Input        : None
# Output       : Prints memory addresses (id) of integers and lists
# Methods      : id(), print()
# Description  : Demonstrates Python’s object caching for integers and new object creation for lists.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

# CASE 1: integers
a = 10
b = 10
print(id(a))   # same id
print(id(b))   # same id

# WHY? Python caches small integers (-5 to 256).
# Both a and b just point to the SAME object in memory.
# It's an optimization — no need to create two copies of 10.

# CASE 2: lists
a = [10]
b = [10]
print(id(a))   # different id
print(id(b))   # different id

# WHY? Lists are mutable objects. Python creates a brand new
# list object every time you write [10], even if contents look
# the same. So a and b live at different addresses.

# Think of it like:
# int 10  → one sticky note, everyone shares it
# [10]    → two separate boxes that happen to contain the same thing

###############################################################################################################################
#
# Application : Illustrates how Python reuses immutable integers but creates new mutable list objects each time.
#
################################################################################################################################
