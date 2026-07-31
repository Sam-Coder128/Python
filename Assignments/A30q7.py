############################################################################################################################
#
# Program      : File Backup every hour
# Functions    : backup_task(), main()
# Input        : Source file path, Destination directory path
# Output       : Backup file created with timestamp, log entry written
# Description  : Uses shutil to copy file with timestamped name, logs backup in backup_log.txt
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
import shutil
import os
from datetime import datetime

def backup_task(src, dest_dir):
    now = datetime.now()
    timestamp = now.strftime("%d_%m_%Y_%H_%M_%S")
    base = os.path.basename(src)
    name, ext = os.path.splitext(base)
    backup_name = f"{name}_{timestamp}{ext}"
    dest_path = os.path.join(dest_dir, backup_name)
    shutil.copy(src, dest_path)
    log_entry = "Backup completed successfully at " + now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n"
    with open("backup_log.txt", "a") as log:
        log.write(log_entry)
    print(log_entry.strip())

def main():
    src = input("Enter source file path: ")
    dest_dir = input("Enter destination directory path: ")
    schedule.every().hour.do(backup_task, src=src, dest_dir=dest_dir)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
