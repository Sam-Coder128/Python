############################################################################################################################
#
# Program      : Datatype, Memory Address and Size Demo
# Input        : 10
# Output       : Datatype : <class 'int'> , Address : (some integer) , Size : 28
# Description  : Displays datatype, memory address and size of an object in Python.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

x = int(input("Enter number: "))

print("Datatype :", type(x))
print("Address  :", id(x))

import sys
print("Size     :", sys.getsizeof(x))

'''
Concept:

type()
Shows the datatype.

id()
Returns the memory identity of the object.

sys.getsizeof()
Returns memory occupied by the object.
'''

###############################################################################################################################
#
# Application : Demonstrates how Python reveals datatype, memory address, and memory size of objects.
#
################################################################################################################################
