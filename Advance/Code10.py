# caesar_cipher.py

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    print(f"Encrypted: {result}")
    return result

def decrypt(cipher, shift):
    result = ""
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    print(f"Decrypted: {result}")
    return result

if __name__ == "__main__":
    text = "Hello, World!"
    shift = 3
    encrypted = encrypt(text, shift)
    decrypt(encrypted, shift)
