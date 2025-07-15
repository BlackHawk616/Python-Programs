# creating a list of squres 

print("Till How Many Numbers You Want To Add The Squares Of That Number In A List")

num = int(input("Enter The Value : "))

sqs = []

for i in range(1,num+1):

    a = i*i

    sqs.append(a)

print(f"The List Of Squares Is {sqs}")