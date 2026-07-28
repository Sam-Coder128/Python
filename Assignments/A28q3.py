############################################################################################################################
#
# Program      : Display File Line by Line
# Functions    : display_file(), main()
# Input        : Demo.txt
# Output       : Displays each line of Demo.txt
# Description  : Accepts a file name and displays contents line by line.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def display_file(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

def main():
    fname = input("Enter file name: ")
    display_file(fname)

if __name__ == "__main__":
    main()
