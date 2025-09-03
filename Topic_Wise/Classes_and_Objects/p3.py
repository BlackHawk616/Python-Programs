# Build a Student class that stores name, roll_no, and marks in 3 subjects. Create objects and print average marks.

class Student:
    def __init__(self, name, roll_no, eng_marks, cs_marks, math_marks):
        self.name = name
        self.roll_no = roll_no
        self.eng_marks = eng_marks
        self.math_marks = math_marks
        self.cs_marks = cs_marks

    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"English Marks : {self.eng_marks}")
        print(f"Maths Marks : {self.math_marks}")
        print(f"Cs Marks : {self.cs_marks}")
    
    def AvgMarks(self, totalmarks):
        total = self.cs_marks + self.eng_marks + self.math_marks
        avg = (total/totalmarks) * 100
        print(f"Average Marks Are {avg}")

name = input("Enter The Name : ")
roll_no = input("Enter The Roll No : ")
eng_marks = int(input("Enter The English Marks : "))
cs_marks = int(input("Enter The Computer Science Marks : "))
math_maths = int(input("Enter The Math Marks : "))

student = Student(name, roll_no, eng_marks, cs_marks, math_maths)
student.showDetails()
student.AvgMarks(300)
