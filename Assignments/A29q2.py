############################################################################################################################
#
# Program      : Display File Contents
# Functions    : display_contents(), main()
# Input        : Demo.txt
# Output       : Display contents of Demo.txt
# Description  : Accepts a file name and displays its contents on console.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def display_contents(filename):
    with open(filename, "r") as f:
        print(f.read())

def main():
    fname = input("Enter file name: ")
    display_contents(fname)

if __name__ == "__main__":
    main()
