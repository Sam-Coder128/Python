############################################################################################################################
#
# Program      : Copy File Contents (Command Line)
# Functions    : copy_file(), main()
# Input        : ABC.txt (command line)
# Output       : Create Demo.txt and copy contents of ABC.txt
# Description  : Accepts existing file name via command line, copies contents into Demo.txt.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import sys

def copy_file(src, dest="Demo.txt"):
    with open(src, "r") as f1, open(dest, "w") as f2:
        f2.write(f1.read())

def main():
    if len(sys.argv) < 2:
        print("Usage: python A29q3.py <sourcefile>")
        return
    src = sys.argv[1]
    copy_file(src)
    print("Contents of", src, "copied into Demo.txt")

if __name__ == "__main__":
    main()
