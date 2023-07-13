#Task 5
#Replace the previous list of users with the following one:

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]
# define a function named show_offers that accepts, again, a username and password as Strings.

# This function will print a message if the user is a Student or anonymous (the get_user function returned None) saying We have great courses to offer you!. If the user is a Teacher it should do nothing.

# Reuse the get_user function from before.

# Use a single conditional (use functions to simplify it or make it more readable).

# Use short-circuiting to avoid errors.
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")

def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None

def show_offers(username, password):
    user = get_user(username, password)
    # The code utilizes short-circuiting by using the not user condition to check if the user is anonymous or not found.
    if not user or user["type"] == "Student":     
        print("We have great courses to offer you!")

show_offers(username, password)