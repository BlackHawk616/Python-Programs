# check_internet_connection.py
import os

def check_internet_connection():
    param = '-n' if os.name == 'nt' else '-c'
    command = f"ping {param} 1 google.com"
    response = os.system(command)
    if response == 0:
        print("Internet connection is active.")
    else:
        print("No internet connection.")

if __name__ == "__main__":
    check_internet_connection()
