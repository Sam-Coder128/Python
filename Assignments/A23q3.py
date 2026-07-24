############################################################################################################################
#
# Program      : Pool Map Even Count Demo
# Functions    : count_even(), main()
# Input        : [1000000,2000000,3000000,4000000]
# Output       : Process ID, Input Number, Even Number Count
# Description  : Uses Pool.map() to count even numbers between 1 and N.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from multiprocessing import Pool
import os

def count_even(n):
    return (os.getpid(), n, n//2)

def main():
    data = [1000000,2000000,3000000,4000000]
    with Pool() as p:
        result = p.map(count_even, data)
    for pid, num, count in result:
        print("Process ID:", pid, "Input Number:", num, "Even Number Count:", count)

if __name__ == "__main__":
    main()
