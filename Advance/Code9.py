# file_searcher.py
import os

def search_files(directory, filename):
    found = False
    for root, dirs, files in os.walk(directory):
        if filename in files:
            print(f"Found: {os.path.join(root, filename)}")
            found = True
    if not found:
        print(f"No files named '{filename}' found in '{directory}'.")

if __name__ == "__main__":
    search_files('.', 'example.txt')
