# Create a Person class with a private attribute _age. Use getter and setter to access and modify it, validating age between 0 and 150.

class Persob:

    def __init__(self,age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, newAge):
        if 0<= newAge >= 150:
            self._age = newAge
        else:
            raise ValueError("The Age Is Out Of Range")