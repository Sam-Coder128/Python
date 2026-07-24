############################################################################################################################
#
# Program      : Pool Map Sum of Even Numbers Demo
# Functions    : sum_even(), main()
# Input        : [1000000,2000000,3000000,4000000]
# Output       : Process ID, Input Number, Sum of Even Numbers
# Description  : Uses Pool.map() to calculate sum of all even numbers from 1 to N.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from multiprocessing import Pool
import os

def sum_even(n):
    total = (n//2) * (n//2 + 1)
    return (os.getpid(), n, total)

def main():
    data = [1000000,2000000,3000000,4000000]
    with Pool() as p:
        result = p.map(sum_even, data)
    for pid, num, total in result:
        print("Process ID:", pid, "Input Number:", num, "Sum of Even Numbers:", total)

if __name__ == "__main__":
    main()
