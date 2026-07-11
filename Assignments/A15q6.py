############################################################################################################################
#
# Program      : Lambda Reduce Minimum Demo
# Input        : [10, 25, 5, 40]
# Output       : 5
# Description  : Lambda function using reduce() to return minimum element.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from functools import reduce

numbers = [10, 25, 5, 40]
minimum = reduce(lambda a, b: a if a < b else b, numbers)
print(minimum)

###############################################################################################################################
#
# Application : Demonstrates lambda with reduce() for finding minimum element.
#
################################################################################################################################
