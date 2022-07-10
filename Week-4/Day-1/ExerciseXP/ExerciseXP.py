# Exercise 1
print("hello world\n"*5)

# Exercise 2
# Instructions
# Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)
result = (99**3)*8
print(result)

# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3 false
# >>> 3 == 3 true
# >>> 3 == "3" false
# >>> "3" > 3 have no idea
# >>> "Hello" == "hello" false

# 🌟 Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: 
# "I have a <computer_brand> computer".

computer_brand = 'Lenovo'
print(f"I have a {computer_brand} computer")

# 🌟 Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. 
# The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "Tal"
age = 26
shoe_size = 42
info = "I learn coding"
sentence = f" My name is {name}, I am {26}y.o. and my show size is {shoe_size}. Also {info}"
print(sentence)

# 🌟 Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a=3
b=2
if a > b:
    print("Hello World")

# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

askForNumber = int(input("Give me a number: "))

if askForNumber % 2 == 0:
    print("That's an even number")
else:
    print("That is an odd number")

# 🌟 Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name,\
# print out a funny message based on the outcome.

nameOfUser = input("What is your name?")
myName = "Tal"
if myName == nameOfUser:
    print("Oh wow!!!\nYou have such a nice name")
else:
    print("I'd recommend you to change the name")

# 🌟 Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

heightInInches = int(input("What is your height in inches? "))
heightInCm = heightInInches * 2.54

if heightInInches > (145/2.54):
    print("You are tall enough to ride")

else:
    print("You need to grow some more")