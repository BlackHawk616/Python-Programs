# Counting A Vowel in the word

word = input("Enter The Word : ")

count = 0 

for w in word:
    if w in ['a','e','i','o','u']:
        count += 1
    else:
        pass

print(f"Number OF Vowels in {word} are {count}")