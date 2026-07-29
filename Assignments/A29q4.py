############################################################################################################################
#
# Program      : Compare Two Files (Command Line)
# Functions    : compare_files(), main()
# Input        : Demo.txt Hello.txt (command line)
# Output       : Success OR Failure
# Description  : Accepts two file names via command line and compares their contents.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import sys

def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        return f1.read() == f2.read()

def main():
    if len(sys.argv) < 3:
        print("Usage: python A29q4.py <file1> <file2>")
        return
    file1, file2 = sys.argv[1], sys.argv[2]
    if compare_files(file1, file2):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()
