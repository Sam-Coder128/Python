############################################################################################################################
#
# Program      : Demo Class Implementation
# Functions    : __init__(), Fun(), Gun(), main()
# Input        : Obj1 = Demo(11,21), Obj2 = Demo(51,101)
# Output       : Displays values of no1 and no2 for both objects
# Description  : Implements a class Demo with instance and class variables, and methods Fun and Gun.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

class Demo:
    Value = 0

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Fun -> no1:", self.no1, "no2:", self.no2)

    def Gun(self):
        print("Gun -> no1:", self.no1, "no2:", self.no2)

def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()
