# Finding The Sum of digits of a number

number = input("Enter The Number : ")

sum = 0

for i in number:
    
    sum+=int(i)

print(f"The Sum of the digit of Number {number} is {sum}")