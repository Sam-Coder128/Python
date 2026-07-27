############################################################################################################################
#
# Program      : Numbers Class Implementation
# Functions    : __init__(), ChkPrime(), ChkPerfect(), Factors(), SumFactors(), main()
# Input        : Value entered by user
# Output       : Displays prime check, perfect check, factors, sum of factors
# Description  : Implements Numbers class with methods to check prime, perfect, factors and sum of factors.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value**0.5)+1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        total = sum(i for i in range(1, self.Value) if self.Value % i == 0)
        return total == self.Value

    def Factors(self):
        print("Factors of", self.Value, ":", [i for i in range(1, self.Value+1) if self.Value % i == 0])

    def SumFactors(self):
        return sum(i for i in range(1, self.Value+1) if self.Value % i == 0)

def main():
    Obj1 = Numbers(28)
    print("Prime:", Obj1.ChkPrime())
    print("Perfect:", Obj1.ChkPerfect())
    Obj1.Factors()
    print("Sum of factors:", Obj1.SumFactors())

    Obj2 = Numbers(17)
    print("Prime:", Obj2.ChkPrime())
    print("Perfect:", Obj2.ChkPerfect())
    Obj2.Factors()
    print("Sum of factors:", Obj2.SumFactors())

if __name__ == "__main__":
    main()
