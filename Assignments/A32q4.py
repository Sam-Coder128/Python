############################################################################################################################
#
# Program      : Copy .txt Files every 10 minutes
# Functions    : copy_txt_files(), main()
# Input        : Source and destination directories
# Output       : Copies .txt files, logs copied files
# Description  : Validates directories, copies only .txt files, logs results
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
import os
import shutil
from datetime import datetime

def copy_txt_files(src, dest):
    if not os.path.isdir(src) or not os.path.isdir(dest):
        print("Invalid directories")
        return
    for file in os.listdir(src):
        if file.endswith(".txt"):
            src_path = os.path.join(src, file)
            dest_path = os.path.join(dest, file)
            try:
                shutil.copy(src_path, dest_path)
                with open("CopyLog.txt", "a") as log:
                    log.write(f"Copied {src_path} to {dest_path} at {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
                print("Copied:", file)
            except Exception as e:
                print("Failed to copy:", file, "-", e)

def main():
    src = input("Enter source directory: ")
    dest = input("Enter destination directory: ")
    schedule.every(10).minutes.do(copy_txt_files, src=src, dest=dest)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
