############################################################################################################################
#
# Program      : Sum and Product Threads Demo
# Functions    : SumThread(), ProductThread()
# Input        : [1, 2, 3, 4]
# Output       : Sum = 10 , Product = 24
# Description  : Creates two threads to compute sum and product of list elements.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import threading

results = {}

def SumThread(lst):
    results['sum'] = sum(lst)

def ProductThread(lst):
    product = 1
    for x in lst:
        product *= x
    results['product'] = product

def main():
    data = [1, 2, 3, 4]
    t1 = threading.Thread(target=SumThread, args=(data,), name="SumThread")
    t2 = threading.Thread(target=ProductThread, args=(data,), name="ProductThread")
    t1.start(); t2.start()
    t1.join(); t2.join()
    print("Sum:", results['sum'])
    print("Product:", results['product'])

if __name__ == "__main__":
    main()
