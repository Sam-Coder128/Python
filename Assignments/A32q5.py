############################################################################################################################
#
# Program      : Delete Empty Files every Hour
# Functions    : delete_empty_files(), main()
# Input        : Directory path
# Output       : Deletes empty files, logs deleted paths
# Description  : Scans directory recursively, deletes zero-byte files, logs results
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
import os
from datetime import datetime

def delete_empty_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    with open("DeletedFilesLog.txt", "a") as log:
                        log.write(f"Deleted {file_path} at {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
                    print("Deleted empty file:", file_path)
            except PermissionError:
                print("Permission denied:", file_path)
            except Exception as e:
                print("Error handling file:", file_path, "-", e)

def main():
    path = input("Enter directory path: ")
    schedule.every().hour.do(delete_empty_files, path)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
