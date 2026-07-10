############################################################################################################################
#
# Program      : Lambda Reduce Maximum Demo
# Input        : [10, 25, 5, 40]
# Output       : 40
# Description  : Lambda function using reduce() to return maximum element.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from functools import reduce

numbers = [10, 25, 5, 40]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)

###############################################################################################################################
#
# Application : Demonstrates lambda with reduce() for finding maximum element.
#
################################################################################################################################
