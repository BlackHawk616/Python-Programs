# get_current_directory_and_files.py
import os

def get_current_directory_and_files():
    cwd = os.getcwd()
    print(f"Current Directory: {cwd}")
    print("Files and Folders:")
    for f in os.listdir(cwd):
        print(f)

if __name__ == "__main__":
    get_current_directory_and_files()
