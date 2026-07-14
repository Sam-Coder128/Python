############################################################################################################################
#
# Program      : Prime Check Demo
# Input        : 5
# Output       : It is Prime Number
# Description  : Checks whether a number is prime.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ChkPrime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "Not Prime"
    return "It is Prime Number"

print(ChkPrime(5))

###############################################################################################################################
#
# Application : Demonstrates prime number checking.
#
################################################################################################################################
