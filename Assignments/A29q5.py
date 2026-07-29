############################################################################################################################
#
# Program      : Frequency of String in File
# Functions    : string_frequency(), main()
# Input        : Demo.txt Marvellous
# Output       : Count how many times "Marvellous" appears in Demo.txt
# Description  : Accepts file name and string, returns frequency of string in file.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def string_frequency(filename, word):
    count = 0
    with open(filename, "r") as f:
        for line in f:
            count += line.split().count(word)
    return count

def main():
    fname = input("Enter file name: ")
    word = input("Enter word to search: ")
    freq = string_frequency(fname, word)
    print("Word", word, "appears", freq, "times in", fname)

if __name__ == "__main__":
    main()
