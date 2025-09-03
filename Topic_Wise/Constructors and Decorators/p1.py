# Write a class Employee with a constructor that initializes name, id, and salary. Add a method to display the employee data.

class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def ShowDetails(self):
        print(f"Name : {self.name}")
        print(f"Id : {self.id}")
        print(f"Salary : {self.salary}")
    
name = "Charan"
iD = 123
salary = 40000000
e = Employee(name,iD, salary)
e.ShowDetails()
        