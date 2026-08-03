############################################################################################################################
#
# Program      : Monitor File Size every 30 seconds
# Functions    : monitor_size(), main()
# Input        : File path
# Output       : Logs file path, size, date and time into FileSizeLog.txt
# Description  : Monitors file size every 30 seconds, handles missing file
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
import os
from datetime import datetime

def monitor_size(path):
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    try:
        size = os.path.getsize(path)
        with open("FileSizeLog.txt", "a") as f:
            f.write(f"File: {path}, Size: {size} bytes, Time: {now}\n")
        print("Logged size for", path)
    except FileNotFoundError:
        print("File does not exist:", path)

def main():
    path = input("Enter file path: ")
    schedule.every(30).seconds.do(monitor_size, path)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
