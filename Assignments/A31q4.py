############################################################################################################################
#
# Program      : Create Log File every 10 minutes
# Functions    : create_log(), main()
# Input        : None
# Output       : Creates log file with timestamped name and content
# Description  : Creates new log file every 10 minutes with creation time
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
from datetime import datetime

def create_log():
    now = datetime.now()
    filename = "MarvellousLog_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    with open(filename, "w") as f:
        f.write("Log file created successfully.\n")
        f.write("Creation Time: " + now.strftime("%d-%m-%Y %I:%M:%S %p"))
    print("Created:", filename)

def main():
    schedule.every(10).minutes.do(create_log)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
