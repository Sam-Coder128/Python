############################################################################################################################
#
# Program      : Perfect Number Check Demo
# Input        : 6
# Output       : Perfect Number
# Description  : Checks whether a number is perfect number or not.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ChkPerfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

ChkPerfect(6)

###############################################################################################################################
#
# Application : Demonstrates how to check if a number is perfect (sum of factors equals number).
#
################################################################################################################################
