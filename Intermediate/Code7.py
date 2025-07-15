# Simple Do-List Using File Handling


def addingList(path):
    with open(path, mode="w") as file1:
        data_list = input("Enter The task : ")
        file1.writelines(data_list)

        print("added Into Simple To-Do List :)")

def ReadList(path):
    with open(path, mode="r") as file2:

        data_list = file2.read()

        print(data_list)

