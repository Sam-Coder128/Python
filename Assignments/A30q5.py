############################################################################################################################
#
# Program      : Write Current Date and Time into Marvellous.txt every 5 minutes
# Functions    : write_task(), main()
# Input        : None
# Output       : Appends execution time into Marvellous.txt every 5 minutes
# Description  : Uses schedule.every(5).minutes.do(...) and datetime module
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
from datetime import datetime

def write_task():
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    with open("Marvellous.txt", "a") as f:
        f.write("Task executed at: " + now + "\n")

def main():
    schedule.every(5).minutes.do(write_task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
