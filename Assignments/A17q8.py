############################################################################################################################
#
# Program      : Increasing Number Pattern Demo
# Input        : 5
# Output       : 1 to 5 in increasing rows
# Description  : Prints increasing number pattern.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def Pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

Pattern(5)

###############################################################################################################################
#
# Application : Demonstrates increasing number pattern printing.
#
################################################################################################################################
