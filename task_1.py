# Task 1:
# Python logical expressions
# Validate the input credentials of a user. You should print the message Welcome, {username}! if the credentials are valid and the message Credentials are invalid if they are not.


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
# Your code here
if valid["username"] == username and valid["password"] == password:
    print(f"Welcome {username}!")
else:
    print("Credentials are invalid")