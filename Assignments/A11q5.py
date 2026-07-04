############################################################################################################################
#
# Program      : Palindrome Check Demo
# Input        : 121
# Output       : Palindrome
# Description  : Checks whether a number is palindrome or not.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ChkPalindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

ChkPalindrome(121)

###############################################################################################################################
#
# Application : Demonstrates how to check if a number is palindrome.
#
################################################################################################################################
