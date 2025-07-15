import string
import random 

def password_generate(length=12):

    if length < 8:
        raise ValueError("The Value Is Less Than Minimum Requirements")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [random.choice(lower), random.choice(upper),random.choice(digits),random.choice(symbols)]

    all_chars = lower + upper + digits + symbols

    password += random.choices(all_chars, k=length-4)

    random.shuffle(password)

    return "".join(password)

print(password_generate(25))