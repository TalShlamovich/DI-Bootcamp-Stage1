# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
userInput = input("Type in a string")

# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

if len(userInput)>10:
    print("String too long")
elif len(userInput)<10:
    print("String not long enough")

# Then, print the first and last characters of the given text.

print(userInput[0])
print(userInput[len(userInput) - 1])

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed.
message = "Hello World"
line = ""
for x in message:
    line += x;
    print(line)