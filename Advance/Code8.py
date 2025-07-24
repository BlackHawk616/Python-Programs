# create_folders.py
import os

def create_folders(base_name, count):
    for i in range(1, count + 1):
        folder_name = f"{base_name}_{i}"
        try:
            os.makedirs(folder_name)
            print(f"Created folder: {folder_name}")
        except FileExistsError:
            print(f"Folder already exists: {folder_name}")

if __name__ == "__main__":
    create_folders("TestFolder", 3)
