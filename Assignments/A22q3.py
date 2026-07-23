############################################################################################################################
#
# Program      : Pool Map Prime Count Demo
# Functions    : is_prime(), prime_count(), main()
# Input        : [10000,20000,30000,40000]
# Output       : Prime counts for each N
# Description  : Uses Pool.map() to count primes between 1 and N for each element in list.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from multiprocessing import Pool

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def prime_count(n):
    return sum(1 for i in range(1, n+1) if is_prime(i))

def main():
    data = [10000,20000,30000,40000]
    with Pool() as p:
        result = p.map(prime_count, data)
    for num, count in zip(data, result):
        print("N:", num, "Prime Count:", count)

if __name__ == "__main__":
    main()
