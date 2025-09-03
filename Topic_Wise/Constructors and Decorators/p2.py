# Create a decorator @validate_positive that checks if all numeric inputs to a method are positive. Apply it to a method in a BankAccount class

class BankAccount:
    def __init__(self):
        self.dep_ammount = 0

    def validate_positive(func):
        def wrapper(*args, **kwags):
            for arg in args[1:]:
                if isinstance(arg, (int, float)) and arg<=0:
                    raise ValueError("The Value Is In Negative")
            return func(*args, **kwags)
        return wrapper
    
    @validate_positive
    def deposit(self, ammount):
        self.dep_ammount += ammount

    
acc = BankAccount()
# acc.deposit(100)      # should work
print(acc.deposit(-50))     # should raise ValueError