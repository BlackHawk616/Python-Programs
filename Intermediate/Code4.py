# Opening A Text File And Reading Its Content


def file_open(path):

    with open(path, mode="+r") as text_file:

        reading = text_file.read()

        print(reading)

file_open("Intermediate/File_Handling/file.txt")    