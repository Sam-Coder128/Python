############################################################################################################################
#
# Program      : Max-Min Threads Demo
# Functions    : MaxThread(), MinThread()
# Input        : [10, 25, 5, 40, 7]
# Output       : Maximum = 40 , Minimum = 5
# Description  : Creates two threads to calculate maximum and minimum element from a list.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import threading

def MaxThread(lst):
    print("Maximum element:", max(lst))

def MinThread(lst):
    print("Minimum element:", min(lst))

def main():
    data = [10, 25, 5, 40, 7]
    t1 = threading.Thread(target=MaxThread, args=(data,), name="MaxThread")
    t2 = threading.Thread(target=MinThread, args=(data,), name="MinThread")
    t1.start(); t2.start()
    t1.join(); t2.join()

if __name__ == "__main__":
    main()
