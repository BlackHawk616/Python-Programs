# Finding Common Elements in a list

try:

    list1 = eval(input("Enter The First List : "))

    list2 = eval(input("Enter The Second List : "))

    common_elements = list(set(list1) & set(list2))

    print(f"The Common Elements In Both The List are {common_elements}")
except Exception as e:
    print(e)
