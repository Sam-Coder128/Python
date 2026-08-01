############################################################################################################################
#
# Program      : Directory Scan every Minute
# Functions    : scan_directory(), main()
# Input        : Directory path
# Output       : Displays directory name, file count, subdirectory count, scan time
# Description  : Uses os module to scan directory every minute
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
import os
from datetime import datetime

def scan_directory(path):
    files = 0
    dirs = 0
    for entry in os.scandir(path):
        if entry.is_file():
            files += 1
        elif entry.is_dir():
            dirs += 1
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    print("Directory Scanned:", path)
    print("Total Files:", files)
    print("Total Subdirectories:", dirs)
    print("Scan Time:", now)

def main():
    path = input("Enter directory path: ")
    schedule.every(1).minutes.do(scan_directory, path)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
