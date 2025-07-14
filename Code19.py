# Sorting a list in asscending order

ul = input("Enter The Numbers Seperated By Commas : ")

ol = [int(x.strip()) for x in ul.split(",")]

ol.sort()

print(ol)