# Writing A User input Into a File

def file_open(path, text):
    with open(path, mode="w") as f:

        f.writelines(text)

text = input("Enter The Data : ")

file_open("Intermediate/File_Handling/file.txt", text)