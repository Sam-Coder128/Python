############################################################################################################################
#
# Program      : Pool Map Sum of Powers Demo
# Functions    : sum_of_powers(), main()
# Input        : [1000000,2000000,3000000,4000000]
# Output       : Sum of fifth powers for each N
# Description  : Uses Pool.map() to calculate 1^5+2^5+...+N^5 for multiple values of N and measure execution time.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from multiprocessing import Pool
import time

def sum_of_powers(n):
    return sum(i**5 for i in range(1, n+1))

def main():
    data = [1000000,2000000,3000000,4000000]
    start = time.time()
    with Pool() as p:
        result = p.map(sum_of_powers, data)
    end = time.time()
    for num, val in zip(data, result):
        print("N:", num, "Sum of powers:", val)
    print("Total Execution Time:", end-start)

if __name__ == "__main__":
    main()
