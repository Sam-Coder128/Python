############################################################################################################################
#
# Program      : Lunch and Wrap up Work Scheduler
# Functions    : lunch_task(), wrapup_task(), main()
# Input        : None
# Output       : Prints Lunch Time! at 1:00 PM and Wrap up work at 6:00 PM
# Description  : Uses schedule.every().day.at(...) for both tasks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time

def lunch_task():
    print("Lunch Time!")

def wrapup_task():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(lunch_task)
    schedule.every().day.at("18:00").do(wrapup_task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
