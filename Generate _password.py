## Generate your password

import secrets
import string

def generate_password(length = 12):
    alphabet = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    return ''.join(secrets.choice(alphabet)
                   for _ in range(length))
password = generate_password()
print("your new password: {password}")


## HIDE you password 

import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

print(f"Username: {username }")
print(f"password : {password}")
