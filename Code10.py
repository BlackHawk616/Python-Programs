# Making A Simple Calculator

a = int(input("Enter The Value Of A : "))
b = int(input("Enter The Value Of B : "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter The Choice : "))

if choice == 1:
    c = a + b 
    print(f"Addition of {a} and {b} is : ", c)

elif choice == 2:
    c = a - b
    print(f"Subtraction of {a} and {b} is : ", c)

elif choice == 3:
    c = a * b
    print(f"Multiplication of {a} and {b} is : ", c)

elif choice == 4:
    c = a/b
    print(f"Division Of {a} and {b} is : ", c)