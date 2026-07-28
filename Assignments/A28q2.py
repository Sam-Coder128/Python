############################################################################################################################
#
# Program      : Count Words in File
# Functions    : count_words(), main()
# Input        : Demo.txt
# Output       : Total number of words in Demo.txt
# Description  : Accepts a file name and counts total number of words in the file.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def count_words(filename):
    with open(filename, "r") as f:
        return sum(len(line.split()) for line in f)

def main():
    fname = input("Enter file name: ")
    total = count_words(fname)
    print("Total number of words in", fname, ":", total)

if __name__ == "__main__":
    main()
