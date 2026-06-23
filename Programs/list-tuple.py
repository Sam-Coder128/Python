############################################################################################################################
#
# Program      : Difference Between List and Tuple Demo
# Input        : None
# Output       : Original List: [10, 20, 30] , Modified List: [100, 20, 30] , Tuple: (10, 20, 30)
# Description  : Demonstrates differences between lists and tuples in Python.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

'''
Difference Between List and Tuple

---------------------------------------------------------
 Feature     | List                     | Tuple
---------------------------------------------------------
Syntax       | [ ]                      | ( )
Mutable      | Yes                      | No
Modification | Allowed                  | Not Allowed
Memory       | Uses more memory         | Uses less memory
Performance  | Slightly slower          | Slightly faster
Use Case     | Changing data            | Fixed data
Example      | Shopping Cart            | Coordinates
---------------------------------------------------------
'''

# List Example
lst = [10, 20, 30]
print("Original List:", lst)

lst[0] = 100
print("Modified List:", lst)

# Tuple Example
tpl = (10, 20, 30)
print("Tuple:", tpl)

# tpl[0] = 100   # Error: Tuple cannot be modified

###############################################################################################################################
#
# Application : Clarifies that lists are mutable and tuples are immutable, with different use cases in Python.
#
################################################################################################################################
