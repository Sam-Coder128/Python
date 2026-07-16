############################################################################################################################
#
# Program      : List Prime Addition Demo
# Input        : 11 elements → 13 5 45 7 4 56 10 34 2 5 8
# Output       : 54
# Description  : Accepts N numbers, stores them in a list, and returns addition of prime numbers.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

# Module: MarvellousNum.py
def ChkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Main Program
import MarvellousNum

def ListPrime(lst):
    total = 0
    for num in lst:
        if MarvellousNum.ChkPrime(num):
            total += num
    return total

n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    data.append(int(input("Enter element: ")))

print("Addition of primes:", ListPrime(data))

###############################################################################################################################
#
# Application : Demonstrates modular programming with prime number checking and summation.
#
################################################################################################################################
