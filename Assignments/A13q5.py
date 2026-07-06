############################################################################################################################
#
# Program      : Grade Display Demo
# Input        : 72
# Output       : First Class
# Description  : Accepts marks and displays grade based on conditions.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

DisplayGrade(72)

###############################################################################################################################
#
# Application : Demonstrates how to assign grades based on marks.
#
################################################################################################################################
