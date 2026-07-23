############################################################################################################################
#
# Program      : Pool Map Factorial Demo
# Functions    : factorial(), main()
# Input        : [10,15,20,25]
# Output       : Process ID, Input Number, Factorial
# Description  : Uses Pool.map() to calculate factorials of multiple numbers simultaneously.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from multiprocessing import Pool, current_process
import os
import math

def factorial(n):
    return (os.getpid(), n, math.factorial(n))

def main():
    data = [10,15,20,25]
    with Pool() as p:
        result = p.map(factorial, data)
    for pid, num, fact in result:
        print("Process ID:", pid, "Input:", num, "Factorial:", fact)

if __name__ == "__main__":
    main()
