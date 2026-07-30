############################################################################################################################
#
# Program      : Print Jay Ganesh every 2 seconds
# Functions    : task(), main()
# Input        : None
# Output       : Jay Ganesh... printed every 2 seconds
# Description  : Uses schedule.every(2).seconds.do(...) to print message repeatedly.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time

def task():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
