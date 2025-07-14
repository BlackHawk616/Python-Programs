# Checking For Palindrome 

num = int(input("Enter The Number To Check Whether its a palidrome or Not\n Enter Here :"))

def check(nu):
    st = str(nu)
    if st[::-1] == st:
        print("The Number Is A Palidrome")
    else:
        print("The Number isnt a palidrome Number Xd")

check(num)