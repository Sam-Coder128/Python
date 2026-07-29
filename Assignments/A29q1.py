############################################################################################################################
#
# Program      : Check File Exists
# Functions    : check_file_exists(), main()
# Input        : Demo.txt
# Output       : Display whether Demo.txt exists or not
# Description  : Accepts a file name and checks if it exists in current directory.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import os

def check_file_exists(filename):
    return os.path.isfile(filename)

def main():
    fname = input("Enter file name: ")
    if check_file_exists(fname):
        print(fname, "exists in current directory.")
    else:
        print(fname, "does not exist in current directory.")

if __name__ == "__main__":
    main()
