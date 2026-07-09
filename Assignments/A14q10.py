############################################################################################################################
#
# Program      : Lambda Largest of Three Demo
# Input        : 10 25 15
# Output       : 25
# Description  : Lambda function to return largest of three numbers.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)
print(largest(10, 25, 15))

###############################################################################################################################
#
# Application : Demonstrates lambda function for finding largest among three numbers.
#
################################################################################################################################
