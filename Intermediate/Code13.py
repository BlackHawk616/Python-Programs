# Creating a timer

import time

seconds = int(input("Enter The Time in Seconds : "))

while seconds:
    print(seconds)
    time.sleep(1)
    seconds-= 1
    
print("Time Up :)")