############################################################################################################################
#
# Program      : Search Word in File
# Functions    : search_word(), main()
# Input        : Demo.txt Marvellous
# Output       : Display whether word is found in Demo.txt
# Description  : Accepts a file name and a word, checks if word is present in file.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def search_word(filename, word):
    with open(filename, "r") as f:
        for line in f:
            if word in line.split():
                return True
    return False

def main():
    fname = input("Enter file name: ")
    word = input("Enter word to search: ")
    found = search_word(fname, word)
    if found:
        print("Word", word, "found in", fname)
    else:
        print("Word", word, "not found in", fname)

if __name__ == "__main__":
    main()
