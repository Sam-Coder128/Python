############################################################################################################################
#
# Program      : Shared Counter with Lock Demo
# Functions    : IncrementCounter()
# Input        : 5 threads, each increments 1000 times
# Output       : Final counter value = 5000
# Description  : Multiple threads increment a shared counter using Lock to avoid race conditions.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import threading

counter = 0
lock = threading.Lock()

def IncrementCounter(times):
    global counter
    for _ in range(times):
        with lock:
            counter += 1

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=IncrementCounter, args=(1000,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Final counter value:", counter)

if __name__ == "__main__":
    main()
