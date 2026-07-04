############################################################################################################################
#
# Program      : Prime Number Check Demo
# Input        : 11
# Output       : Prime Number
# Description  : Checks whether a number is prime or not.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ChkPrime(n):
    if n < 2:
        print("Not Prime")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime Number")

ChkPrime(11)

###############################################################################################################################
#
# Application : Demonstrates how to check if a number is prime.
#
################################################################################################################################
