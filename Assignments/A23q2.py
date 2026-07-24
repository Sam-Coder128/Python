############################################################################################################################
#
# Program      : Pool Map Sum of Odd Numbers Demo
# Functions    : sum_odd(), main()
# Input        : [1000000,2000000,3000000,4000000]
# Output       : Process ID, Input Number, Sum of Odd Numbers
# Description  : Uses Pool.map() to calculate sum of all odd numbers from 1 to N.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from multiprocessing import Pool
import os

def sum_odd(n):
    count = (n+1)//2
    total = count * count
    return (os.getpid(), n, total)

def main():
    data = [1000000,2000000,3000000,4000000]
    with Pool() as p:
        result = p.map(sum_odd, data)
    for pid, num, total in result:
        print("Process ID:", pid, "Input Number:", num, "Sum of Odd Numbers:", total)

if __name__ == "__main__":
    main()
