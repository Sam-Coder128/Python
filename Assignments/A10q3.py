############################################################################################################################
#
# Program      : Factorial Calculation Demo
# Input        : 5
# Output       : 120
# Description  : Prints factorial of a given number.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

Factorial(5)

###############################################################################################################################
#
# Application : Demonstrates how to calculate factorial of a number using iteration.
#
################################################################################################################################
