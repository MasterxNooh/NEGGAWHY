import random
import string

def generate_password(length=12, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()?"

    characters = letters + digits
    if use_symbols:
        characters += symbols

    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Welcome to Password Generator!")
length = int(input("Enter password length: "))
choice = input("Do you want symbols in the password? (y/n): ").lower()

if choice == "y":
    password = generate_password(length, use_symbols=True)
else:
    password = generate_password(length, use_symbols=False)

print(f"\n✅ Your generated password is: {password}")
