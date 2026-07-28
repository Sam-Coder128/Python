############################################################################################################################
#
# Program      : Count Lines in File
# Functions    : count_lines(), main()
# Input        : Demo.txt
# Output       : Total number of lines in Demo.txt
# Description  : Accepts a file name and counts how many lines are present in the file.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def count_lines(filename):
    with open(filename, "r") as f:
        return sum(1 for _ in f)

def main():
    fname = input("Enter file name: ")
    total = count_lines(fname)
    print("Total number of lines in", fname, ":", total)

if __name__ == "__main__":
    main()
