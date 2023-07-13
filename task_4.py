# Python logical expressions
# Task 4:#  define a function named get_user with the input arguments username and password, both as a String.
#There is a global variable named users as a list of dictionaries:

users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]
# The function should return the first dictionary in the list users matching the username and password provided. If no user matches, it should return None.
#When the user provided is invalid (when get_user returned None) the function should show the message An error occurred. You are not authorized..
#Do nothing if the user is valid.
#Use the "truthy" and "falsy" nature of the Non-boolean values returned by get_user.
def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
user = get_user(username, password)

if not user:
    print("An error occurred. You are not authorized.")

        
    




    