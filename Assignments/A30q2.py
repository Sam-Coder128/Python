############################################################################################################################
#
# Program      : Display Current Date and Time every minute
# Functions    : show_datetime(), main()
# Input        : None
# Output       : Current Date and Time printed every minute
# Description  : Uses datetime module and schedule.every(1).minutes.do(...)
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
from datetime import datetime

def show_datetime():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    schedule.every(1).minutes.do(show_datetime)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
