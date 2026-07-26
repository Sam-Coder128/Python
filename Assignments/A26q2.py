############################################################################################################################
#
# Program      : Circle Class Implementation
# Functions    : __init__(), Accept(), CalculateArea(), CalculateCircumference(), Display(), main()
# Input        : Radius entered by user
# Output       : Displays Radius, Area, Circumference
# Description  : Implements Circle class with methods to accept radius, calculate area and circumference, and display results.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius:", self.Radius, "Area:", self.Area, "Circumference:", self.Circumference)

def main():
    Obj1 = Circle()
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2 = Circle()
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

if __name__ == "__main__":
    main()
