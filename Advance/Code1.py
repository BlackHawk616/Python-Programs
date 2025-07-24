# Creating A Rock Papers Scissors
import random 

def welcome():
    print("Welcome To Rock, Paper Scissors")
    print("These Are The Options To Choose")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
welcome()

choice = int(input("Enter The Choice : "))

player_choice = ""

if choice == 1:
    player_choice += "Rock"
elif choice == 2:
    player_choice += "Paper"
elif choice == 3:
    player_choice += "Scissors"

def brain(choice):
    choices = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(choices)

    if computer_choice == choice:
        print("Tie, Both Choose Same option")

    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print("You Won, Computer Chosse Scissors")
        elif computer_choice == "Paper":
            print("You Lose, Computer Chosse Paper")


    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("You Won, Computer Chosse Paper")
        elif computer_choice == "Rock":
            print("You Lose, Computer Chosse Rock")
    
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("You Won, Computer Chosse Rock")
        elif computer_choice == "Scissors":
            print("You Lose, Computer Chosse Scissors")


brain(player_choice)