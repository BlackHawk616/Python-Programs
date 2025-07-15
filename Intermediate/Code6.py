# Counting Lines and Words In A File 

def countLines(path):
    with open(path,mode="r") as f:
        dat = f.readlines()
        CountLines = 0
        for i in dat:
            CountLines+=1
            print(i)

        print(f"The Total Lines In The Files Are {CountLines}")

countLines("Intermediate/File_Handling/file.txt")

def CountWords(path):
    with open(path, mode="r") as f1:
        dt = f1.read().split(" ")
        countWords = 0
        for i in dt:
            countWords+= 1
        print(f"The Total Words In The File Are {countWords}")
            

CountWords("Intermediate/File_Handling/file.txt")