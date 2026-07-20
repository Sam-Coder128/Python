############################################################################################################################
#
# Program      : EvenFactor and OddFactor Threads Demo
# Input        : 12
# Output       : Sum of even factors = 18 , Sum of odd factors = 13
# Description  : Creates two threads to calculate sum of even and odd factors of a number.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import threading

def EvenFactor(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            total += i
    print("Sum of even factors:", total)

def OddFactor(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            total += i
    print("Sum of odd factors:", total)

num = int(input("Enter number: "))

t1 = threading.Thread(target=EvenFactor, args=(num,), name="EvenFactor")
t2 = threading.Thread(target=OddFactor, args=(num,), name="OddFactor")

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")

###############################################################################################################################
#
# Application : Demonstrates concurrent threads calculating even and odd factors.
#
################################################################################################################################
