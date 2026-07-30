############################################################################################################################
#
# Program      : Print Coding Kar..! every 30 minutes
# Functions    : task(), main()
# Input        : None
# Output       : Coding Kar..! printed every 30 minutes
# Description  : Uses schedule.every(30).minutes.do(...)
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time

def task():
    print("Coding Kar..!")

def main():
    schedule.every(30).minutes.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
