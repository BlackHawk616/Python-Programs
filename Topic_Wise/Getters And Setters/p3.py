# Implement a class Car with a private attribute _speed. Use setter to ensure speed cannot be negative.

class Car:
    
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return f"Car's Speed Is {self._speed}"
    
    @speed.setter
    def speed(self, speed):
        if speed < 0:
            raise ValueError("Speec Cant Be Negative")
        self._speed = speed