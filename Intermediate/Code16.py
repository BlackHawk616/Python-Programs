# Remove punctuation from a string
import string

s = input("Enter The Sentance With Puncation ")
no_punct = "".join(c for c in s if c not in string.punctuation)
print(no_punct)
