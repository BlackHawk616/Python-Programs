# Number Guessing

from random import randint

def guess_number(num):

    random_num = randint(1,11)

    if num == random_num:
        print("Congratulations, You Won")
    else:
        print(f"Sorry, You Lose. The Number Was {random_num}")
    
n = int(input("Enter The Number btw 1 and 10 : "))

guess_number(n)