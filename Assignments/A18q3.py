############################################################################################################################
#
# Program      : List Minimum Demo
# Input        : 4 elements → 13 5 45 7
# Output       : 5
# Description  : Accepts N numbers, stores them in a list, and returns minimum element.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ListMinimum(lst):
    return min(lst)

n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    data.append(int(input("Enter element: ")))

print("Minimum:", ListMinimum(data))

###############################################################################################################################
#
# Application : Demonstrates how to find minimum element in a list.
#
################################################################################################################################
