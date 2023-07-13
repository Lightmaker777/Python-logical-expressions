# Python logical expressions
# Task 3:
#We now want a version of the first task, that will implement an "open doors" policy on the weekends. So, if the user credentials are valid, or the date is on the weekend, the conditional should evaluate to True and greet the user.

# using a single logical expression.

# reusing the isweekend(<Datetime>) function from before.
import datetime
from datetime import date

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
#today = datetime.date(2021, 8, 7)
today = datetime.date(2021, 8, 6)
# Your code here
def isweekend():
    if (valid["username"] == username and valid["password"] == password) or today.weekday() == 5 or today.weekday() == 6:
        print(f"Welcome {username}!")
    else:
        print("Credentials are invalid")
        
isweekend()

