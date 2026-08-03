############################################################################################################################
#
# Program      : Create New Text File every Minute
# Functions    : create_file(), main()
# Input        : None
# Output       : Creates file with timestamped name and writes filename, creation date, creation time
# Description  : Uses schedule.every(1).minutes.do(...) to create new file with timestamp
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
from datetime import datetime

def create_file():
    now = datetime.now()
    filename = "File_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    with open(filename, "w") as f:
        f.write("Filename: " + filename + "\n")
        f.write("Creation Date: " + now.strftime("%d-%m-%Y") + "\n")
        f.write("Creation Time: " + now.strftime("%I:%M:%S %p") + "\n")
    print("Created:", filename)

def main():
    schedule.every(1).minutes.do(create_file)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
