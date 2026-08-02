############################################################################################################################
#
# Program      : Directory File Count every 5 minutes
# Functions    : count_files(), main()
# Input        : Directory path
# Output       : Appends directory path, file count, date and time into DirectoryCountLog.txt
# Description  : Counts files in directory every 5 minutes and logs result
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
import os
from datetime import datetime

def count_files(path):
    files = sum(1 for entry in os.scandir(path) if entry.is_file())
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    with open("DirectoryCountLog.txt", "a") as f:
        f.write(f"Directory: {path}, Files: {files}, Time: {now}\n")
    print("Logged file count for", path)

def main():
    path = input("Enter directory path: ")
    schedule.every(5).minutes.do(count_files, path)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
