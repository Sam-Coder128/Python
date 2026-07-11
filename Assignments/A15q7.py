############################################################################################################################
#
# Program      : Lambda Filter String Length Demo
# Input        : ["apple", "banana", "grapes", "pineapple"]
# Output       : ['banana', 'pineapple']
# Description  : Lambda function using filter() to return strings with length > 5.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

strings = ["apple", "banana", "grapes", "pineapple"]
long_strings = list(filter(lambda s: len(s) > 5, strings))
print(long_strings)

###############################################################################################################################
#
# Application : Demonstrates lambda with filter() for selecting strings longer than 5 characters.
#
################################################################################################################################
