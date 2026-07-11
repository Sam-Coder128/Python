############################################################################################################################
#
# Program      : Lambda Filter Even Count Demo
# Input        : [1, 2, 3, 4, 5, 6]
# Output       : 3
# Description  : Lambda function using filter() to count even numbers in a list.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(len(evens))

###############################################################################################################################
#
# Application : Demonstrates lambda with filter() for counting even numbers in a list.
#
################################################################################################################################
