# Simple Grade Calculator

def Grades(total_marks):

    grades = ['A+','A','B+','B','C','F']

    if total_marks >= 95:
        print(f"Your Grade Is {grades[0]}")

    elif total_marks >= 90 and total_marks < 95:
        print(f"Your Grade Is {grades[1]}")
    
    elif total_marks >= 80 and total_marks < 90:
        print(f"Your Grade Is {grades[2]}")
    
    elif total_marks >= 70 and total_marks < 80:
        print(f"Your Grade Is {grades[3]}")
    
    elif total_marks >= 60 and total_marks < 70:
        print(f"Your Grade Is {grades[4]}")
    elif total_marks >= 50 and total_marks < 60:
        print(f"Your Grade Is {grades[5]}")
    
    
    
    
