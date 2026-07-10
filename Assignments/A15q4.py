############################################################################################################################
#
# Program      : Lambda Reduce Addition Demo
# Input        : [1, 2, 3, 4]
# Output       : 10
# Description  : Lambda function using reduce() to return sum of elements.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)
print(total)

###############################################################################################################################
#
# Application : Demonstrates lambda with reduce() for summing list elements.
#
################################################################################################################################
