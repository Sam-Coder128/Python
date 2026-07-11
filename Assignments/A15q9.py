############################################################################################################################
#
# Program      : Lambda Reduce Product Demo
# Input        : [1, 2, 3, 4]
# Output       : 24
# Description  : Lambda function using reduce() to return product of elements.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print(product)

###############################################################################################################################
#
# Application : Demonstrates lambda with reduce() for multiplying list elements.
#
################################################################################################################################
