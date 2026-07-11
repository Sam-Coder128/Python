############################################################################################################################
#
# Program      : Lambda Filter Divisible by 3 and 5 Demo
# Input        : [10, 15, 20, 30, 45]
# Output       : [15, 30, 45]
# Description  : Lambda function using filter() to return numbers divisible by both 3 and 5.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

numbers = [10, 15, 20, 30, 45]
divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(divisible)

###############################################################################################################################
#
# Application : Demonstrates lambda with filter() for selecting numbers divisible by 3 and 5.
#
################################################################################################################################
