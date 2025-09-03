# Build a class Temperature to store Celsius, and use getters to convert it to Fahrenheit.

class Temperature:

    def __init__(self, celsisus):
        self._temp = celsisus

    @property
    def tempValue(self):
        return self._temp
   
    @property
    def fahrenheit(self):
        return (self._temp * 9/5) + 32
    
    