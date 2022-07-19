# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
from datetime import date, time, datetime

import string
import random

def exercise1 ():
    user_num = int(input("Give me a number >>> "))
    comp_num = random.randint(1,101)
    if user_num == comp_num:
        print("well done")
        return True
    else:
        print("sorry")
        return False

# exercise1()

# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

print(''.join(random.choices(string.ascii_letters, k=5)))

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

today = date.today()
print("Today's date:", today)

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

a = today
b = date(2023,1,1)
print(b-a)

# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice),
# then displays a message stating how many minutes the user lived in his life.

birthdate = datetime(1995, 11 , 15, 00, 00, 00)
today = datetime.now()
difference = today - birthdate
difference_in_sec = difference.total_seconds
minutes = divmod(difference_in_sec(), 60)[0]
print('minutes')
print(minutes)