############################################################################################################################
#
# Program      : Display Message using Function
# Functions    : DisplayMessage(), main()
# Input        : Message from user
# Output       : Prints message every 5 seconds
# Description  : Uses schedule.every(5).seconds.do(DisplayMessage, message)
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
    message = input("Enter message: ")
    schedule.every(5).seconds.do(DisplayMessage, message)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
