# Checking an Element In The List

Lst = eval(input("Enter The Value Of List : "))

Element = int(input("Enter The Element You Want To Check"))

def checking(lst, element):
    if element in lst:
        print(f"The Element {Element} is in the list")
    else:
        print("THe Element Is Not In The List")
        
checking(Lst,Element)