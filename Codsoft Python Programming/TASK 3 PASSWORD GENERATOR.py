import random
import string

def generate_password(length, include_digits=True, include_special_characters=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))

    if length <= 0:
        print("Invalid length. Please enter a positive integer.")
        return

    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_characters = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_digits, include_special_characters)
    print("Generated Password:", password)


password_generator()
