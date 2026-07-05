############################################################################################################################
#
# Program      : Vowel or Consonant Check Demo
# Input        : a
# Output       : Vowel
# Description  : Accepts one character and checks whether it is vowel or consonant.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def ChkVowel(ch):
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")

ChkVowel('a')

###############################################################################################################################
#
# Application : Demonstrates how to check if a character is vowel or consonant.
#
################################################################################################################################
