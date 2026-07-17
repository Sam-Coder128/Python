############################################################################################################################
#
# Program      : Filter-Map-Reduce Prime Demo
# Input        : [2, 70, 11, 10, 17, 23, 31, 77]
# Output       : Filter → [2, 11, 17, 23, 31] , Map → [4, 22, 34, 46, 62] , Reduce → 62
# Description  : Filters prime numbers, maps to double, reduces to maximum.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = [2, 70, 11, 10, 17, 23, 31, 77]

filtered = list(filter(is_prime, numbers))
print("List after filter:", filtered)

mapped = list(map(lambda x: x * 2, filtered))
print("List after map:", mapped)

maximum = reduce(lambda a, b: a if a > b else b, mapped)
print("Output of reduce:", maximum)

###############################################################################################################################
#
# Application : Demonstrates filter-map-reduce pipeline with prime numbers.
#
################################################################################################################################
