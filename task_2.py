# Python logical expressions
# Task 2:
# Define a function named isweekend that accepts a parameter named date of type Datetime (with a default value of datetime.datetime.now()).

# This function will serve as a logical expression and will return True if the day of the week in the date is either Saturday or Sunday. It will return False in any other case.
 
# required to use the OR operator
import datetime
def isweekend(date=datetime.datetime.now()):
    if date.weekday() == 5 or date.weekday() == 6:
        return True
    else:
        return False
#test cases:
print(isweekend(datetime.date(2021, 8, 6)))
print(isweekend(datetime.date(2021, 8, 7)))
print(isweekend(datetime.date(2021, 8, 8)))
print(isweekend(datetime.date(2021, 8, 9)))

