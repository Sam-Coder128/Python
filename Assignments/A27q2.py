############################################################################################################################
#
# Program      : BankAccount Class Implementation
# Functions    : __init__(), Display(), Deposit(), Withdraw(), CalculateInterest(), main()
# Input        : Account holder name and initial balance
# Output       : Displays account details, deposits, withdrawals, and interest
# Description  : Implements BankAccount class with Name, Amount and class variable ROI.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder:", self.Name, "Balance:", self.Amount)

    def Deposit(self, amt):
        self.Amount += amt
        print("Deposited:", amt, "New Balance:", self.Amount)

    def Withdraw(self, amt):
        if amt <= self.Amount:
            self.Amount -= amt
            print("Withdrawn:", amt, "New Balance:", self.Amount)
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest:", interest)
        return interest

def main():
    Obj1 = BankAccount("Samruddh", 1000)
    Obj1.Display()
    Obj1.Deposit(500)
    Obj1.Withdraw(300)
    Obj1.CalculateInterest()

    Obj2 = BankAccount("Piyush", 2000)
    Obj2.Display()
    Obj2.Deposit(1000)
    Obj2.Withdraw(5000)
    Obj2.CalculateInterest()

if __name__ == "__main__":
    main()
