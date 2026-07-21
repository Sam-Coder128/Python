############################################################################################################################
#
# Program      : Prime and NonPrime Threads Demo
# Functions    : is_prime(), PrimeThread(), NonPrimeThread()
# Input        : [10, 11, 12, 13, 14, 15]
# Output       : Prime → 11, 13 ; NonPrime → 10, 12, 14, 15
# Description  : Creates two threads to display prime and non-prime numbers from a list.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import threading

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def PrimeThread(lst):
    primes = [x for x in lst if is_prime(x)]
    print("Prime numbers:", primes)

def NonPrimeThread(lst):
    nonprimes = [x for x in lst if not is_prime(x)]
    print("Non-prime numbers:", nonprimes)

def main():
    data = [10, 11, 12, 13, 14, 15]
    t1 = threading.Thread(target=PrimeThread, args=(data,), name="Prime")
    t2 = threading.Thread(target=NonPrimeThread, args=(data,), name="NonPrime")
    t1.start(); t2.start()
    t1.join(); t2.join()

if __name__ == "__main__":
    main()
