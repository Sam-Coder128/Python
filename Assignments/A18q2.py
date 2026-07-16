############################################################################################################################
#
# Program      : List Maximum Demo
# Input        : 7 elements → 13 5 45 7 4 56 34
# Output       : 56
# Description  : Accepts N numbers, stores them in a list, and returns maximum element.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ListMaximum(lst):
    return max(lst)

n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    data.append(int(input("Enter element: ")))

print("Maximum:", ListMaximum(data))

###############################################################################################################################
#
# Application : Demonstrates how to find maximum element in a list.
#
################################################################################################################################
