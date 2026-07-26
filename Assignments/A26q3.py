############################################################################################################################
#
# Program      : Arithmetic Class Implementation
# Functions    : __init__(), Accept(), Addition(), Subtraction(), Multiplication(), Division(), main()
# Input        : Values entered by user
# Output       : Displays results of addition, subtraction, multiplication, division
# Description  : Implements Arithmetic class with methods to accept values and perform basic operations.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1: "))
        self.Value2 = int(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        return self.Value1 / self.Value2

def main():
    Obj1 = Arithmetic()
    Obj1.Accept()
    print("Addition:", Obj1.Addition())
    print("Subtraction:", Obj1.Subtraction())
    print("Multiplication:", Obj1.Multiplication())
    print("Division:", Obj1.Division())

    Obj2 = Arithmetic()
    Obj2.Accept()
    print("Addition:", Obj2.Addition())
    print("Subtraction:", Obj2.Subtraction())
    print("Multiplication:", Obj2.Multiplication())
    print("Division:", Obj2.Division())

if __name__ == "__main__":
    main()
