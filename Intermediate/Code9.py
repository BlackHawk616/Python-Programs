# Sum Of Even Numbers In The List

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

summ = 0

for i in lst:
    if i%2 == 0:

        summ+=i
    else:
        continue


print(summ)