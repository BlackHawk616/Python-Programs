# Implement a class BankAccount with protected attribute _balance. Inherit a class SavingsAccount that adds interest calculation.
class BankAccount:
    
    def __init__(self, balance, interst, time):
        self._balance = balance
        self.intrest = interst
        self.time = time
    @property
    def Balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def savings(self):
        return self._balance * self.intrest * self.time
    
    