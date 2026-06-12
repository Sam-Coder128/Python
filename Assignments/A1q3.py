############################################################################################################################
#
# Program      : Object Identity with id()
# Input        : None
# Output       : Prints True/False comparisons of object identities
# Methods      : id(), print()
# Description  : Demonstrates how Python assigns memory addresses differently for integers, lists, and strings.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

# id() returns the memory address of an object as an integer.
# In CPython (standard Python), it's literally the address
# in RAM where that object lives.

# Is it the same for two variables with the same value?
# DEPENDS on the type:

# Small integers (cached): YES, same id
a = 10
b = 10
print(id(a) == id(b))    # True — cached object, shared reference

# Large integers (not cached): NO, different id
a = 1000
b = 1000
print(id(a) == id(b))    # False — two separate int objects

# Lists: always different id even with same contents
a = [1, 2]
b = [1, 2]
print(id(a) == id(b))    # False

# Short strings: often same id (interned by Python)
# Conclusion: same VALUE does NOT guarantee same id.
# It's an implementation detail, not a language rule.

###############################################################################################################################
#
# Application : Shows how Python reuses cached small integers and interned strings, but creates new objects for large integers and lists.
#
################################################################################################################################
