############################################################################################################################
#
# Program      : List Addition Demo
# Input        : 6 elements → 13 5 45 7 4 56
# Output       : 130
# Description  : Accepts N numbers, stores them in a list, and returns addition of all elements.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ListAddition(lst):
    return sum(lst)

n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    data.append(int(input("Enter element: ")))

print("Addition:", ListAddition(data))

###############################################################################################################################
#
# Application : Demonstrates how to calculate sum of list elements.
#
################################################################################################################################
