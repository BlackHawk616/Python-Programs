# Checking whether The Program is a prime number Or not

def Check(num):
    if num < 2 :
        print("Number is not a prime ")
    if num == 2:
        print("Number Is A Prime Number ")

    if num%2 == 0:
        print("No this is not a prime Number")

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Its Not A Prime Number")

Check(5)