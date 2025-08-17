#Randon Password Generator
import random , string

#Step-1: Define Password Generator Function

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password lenght must be atleast 4 characters.")
    #Character sets for password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_character = string.punctuation

    #Ensure at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_character)
    ]

    #Fill the remaing lenght with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_character
    password += random.choices(all_chars, k = length - 4)

    #Shuffle the password to make it more random
    random.shuffle(password)

    #Convert the list to a string and return
    return ''.join(password)

#Step-2: User interaction

try:
    length = int(input("Enter the desired password length (minimum 4):"))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError as e:
    print(e)
