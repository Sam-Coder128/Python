############################################################################################################################
#
# Program      : Print Namskar every day at 9:00 AM
# Functions    : task(), main()
# Input        : None
# Output       : Namskar... printed daily at 9:00 AM
# Description  : Uses schedule.every().day.at("09:00").do(...)
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time

def task():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00").do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
