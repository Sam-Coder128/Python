############################################################################################################################
#
# Program      : Display Message at Interval
# Functions    : display_message(), main()
# Input        : Message and interval in seconds
# Output       : Prints message repeatedly after interval
# Description  : Accepts message and interval, validates interval > 0, schedules task.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import schedule
import time

def display_message(msg):
    print(msg)

def main():
    message = input("Enter message: ")
    interval = int(input("Enter interval in seconds: "))
    if interval <= 0:
        print("Interval must be greater than zero.")
        return
    schedule.every(interval).seconds.do(display_message, message)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
