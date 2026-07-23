############################################################################################################################
#
# Program      : Pool Map Sum of Squares Demo
# Functions    : sum_of_squares(), main()
# Input        : [1000000,2000000,3000000,4000000]
# Output       : [333333833333500000, 2666668666667000000, ...]
# Description  : Uses Pool.map() to calculate sum of squares from 1 to N for each element in list.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from multiprocessing import Pool

def sum_of_squares(n):
    return (n*(n+1)*(2*n+1))//6

def main():
    data = [1000000,2000000,3000000,4000000]
    with Pool() as p:
        result = p.map(sum_of_squares, data)
    print(result)

if __name__ == "__main__":
    main()
