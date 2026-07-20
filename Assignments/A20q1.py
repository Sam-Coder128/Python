############################################################################################################################
#
# Program      : Even and Odd Threads Demo
# Input        : None
# Output       : First 10 even and odd numbers
# Description  : Creates two threads (Even, Odd) to display first 10 even and odd numbers.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import threading

def Even():
    for i in range(2, 21, 2):
        print("Even:", i)

def Odd():
    for i in range(1, 20, 2):
        print("Odd :", i)

t1 = threading.Thread(target=Even, name="Even")
t2 = threading.Thread(target=Odd, name="Odd")

t1.start()
t2.start()

t1.join()
t2.join()

###############################################################################################################################
#
# Application : Demonstrates concurrent execution of two threads for even and odd numbers.
#
################################################################################################################################
