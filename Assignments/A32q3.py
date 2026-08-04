############################################################################################################################
#
# Program      : Read and Display File every Minute
# Functions    : read_file(), main()
# Input        : File path
# Output       : Displays contents or handles errors (missing, empty, permission denied)
# Description  : Reads file every minute, handles exceptions gracefully
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time
from datetime import datetime

def read_file(path):
    try:
        with open(path, "r") as f:
            content = f.read()
            if not content.strip():
                print("File is empty:", path)
            else:
                print("Contents of", path, ":\n", content)
    except FileNotFoundError:
        print("File does not exist:", path)
    except PermissionError:
        print("Permission denied:", path)
    except OSError:
        print("File cannot be opened:", path)

def main():
    path = input("Enter file path: ")
    schedule.every(1).minutes.do(read_file, path)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
