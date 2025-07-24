# generate_otp.py
import random

def generate_otp(length=6):
    otp = ''.join(str(random.randint(0, 9)) for _ in range(length))
    print(f"Generated OTP: {otp}")
    return otp

if __name__ == "__main__":
    generate_otp(6)
