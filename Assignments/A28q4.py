############################################################################################################################
#
# Program      : Copy File Contents
# Functions    : copy_file(), main()
# Input        : ABC.txt Demo.txt
# Output       : Contents of ABC.txt copied into Demo.txt
# Description  : Accepts two file names and copies contents from first file into second file.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def copy_file(src, dest):
    with open(src, "r") as f1, open(dest, "w") as f2:
        f2.write(f1.read())

def main():
    src = input("Enter source file name: ")
    dest = input("Enter destination file name: ")
    copy_file(src, dest)
    print("Contents of", src, "copied into", dest)

if __name__ == "__main__":
    main()
