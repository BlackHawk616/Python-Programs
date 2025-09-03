#Create a base class Vehicle with attributes brand and model. Inherit it in a class Bike and add a method get_full_name().

class Vehicle:

    def __init__(self, bname, model):
        self.brandname = bname
        self.modelname = model


class Bike(Vehicle):
    def get_full_name(self):
        return f"{self.brandname} and {self.modelname}"
        

v = Bike("ducati", "Panigale V4S")
print(v.get_full_name())