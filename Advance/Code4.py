# Rename a file using OS module

import os

def rename_file(old_name, new_name):
    
    if not os.path.isfile(old_name):
        raise FileNotFoundError(f"The file '{old_name}' does not exist.")
    if os.path.exists(new_name):
        raise FileExistsError(f"A file named '{new_name}' already exists.")
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}'.")

