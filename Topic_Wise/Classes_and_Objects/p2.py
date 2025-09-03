# Write a class Rectangle with length and width attributes. Add methods to compute area and perimeter.

class Rectangle:

    def __init__(self, length, width):
        self.lenght = float(length)
        self.width = float(width)

    def Area(self):
        area = self.lenght * self.width
        print(f"The Area Of A Rectange with {self.lenght} leght and {self.width} width is {area}")

    def perimeter(self):
        perimeter = 2 * (self.lenght + self.width)
        print(f"The Perimeter Of A Rectange with {self.lenght} leght and {self.width} width is {perimeter}")

lenght = int(input("Enter The Length Of The Rectangle : "))
width = int(input("Enter The Width of the Rectangle : "))

rec = Rectangle(lenght, width)
rec.Area()
rec.perimeter()