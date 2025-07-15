# Creating A Simple login System

print("Choose The Options You Want To Procced")
print("1. Create A New User And Password")
print("2. Login In Into An Exisiting Account")

Users = []
Password = []

def new_user(name,password):
    Users.append(name)

    Password.append(password)

def login():
    username = input("Enter The User Name : ")

    if username in Users:

        print("Please Enter The Password")

        passwrd = input("enter The Password : ")

        if passwrd in Password:

            print("Loggin Successful!")
        
        else:
            print("Wrong Password1 Try Again Later")

    else:
        print("Please Creater A New User")


def main():

    while True: 

        option = int(input("Enter The Option : "))

        if option == 1:
            name = input("Enter Username : ")
            passw = input("Enter New Password : ")

            new_user(name,passw)
        elif option == 2:
            login()

        else:
            pass


main()