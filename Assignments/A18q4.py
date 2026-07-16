############################################################################################################################
#
# Program      : List Frequency Demo
# Input        : 11 elements → 13 5 45 7 4 56 5 34 2 5 65
# Output       : 3
# Description  : Accepts N numbers, stores them in a list, and returns frequency of a given element.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ListFrequency(lst, element):
    return lst.count(element)

n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    data.append(int(input("Enter element: ")))

search = int(input("Enter element to search: "))
print("Frequency:", ListFrequency(data, search))

###############################################################################################################################
#
# Application : Demonstrates how to calculate frequency of an element in a list.
#
################################################################################################################################
