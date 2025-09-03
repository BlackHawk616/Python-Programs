# Implement a Product class with a constructor that auto-assigns unique product IDs using a class-level counter.

class Product:

    id_counter = 1
    
    def __init__(self, pname):
        self.pname = pname
        self.id = Product.id_counter
        Product.id_counter+=1

p1 = Product("Laptop")
p2 = Product("Phone")
p3 = Product("Tablet")

print(p1.pname, p1.id)   # Laptop 1
print(p2.pname, p2.id)   # Phone 2
print(p3.pname, p3.id)   # Tablet 3