import random
import string
import secrets  # Add this import for secrets module

# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)

def generate_password(length):
    password = ''
    # Generate password
    for _ in range(length):
        password += secrets.choice(all_characters)
    return password
