# Count a word in sentance

sentance = input("Enter The Sentance : ")

sl = sentance.split(" ")

word = input("Enter The Word You Want to Search In The Sentance : ")
count = 0
for w in sl:
    if w == word:
        count+=1
    else:
        continue
print(f"The Word {word} as been repated {count} times")