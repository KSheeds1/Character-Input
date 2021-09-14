import datetime


"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
# Get users name
name = input("What is your name? ")

# Get users age
age = int(input("Please enter your age: "))

# Get current year
current_year = datetime.datetime.now()

# Get difference between users age and 100 years
age_difference = str((current_year.year - age)+100)

# Provide user with the year that they wil turn 100 years old
print(f'{name}, you will be 100 years old in the year {age_difference}.')
