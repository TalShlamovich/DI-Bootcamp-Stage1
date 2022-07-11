# Instructions
# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

from xxlimited import new


userNumber = int(input("Give me a number: "))
length = int(input("Give me another number: "))
multiples = []
for i in range(1, length+1):
    multiples.append(userNumber*i)
print(multiples)

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

userString = input("Give me a string: ")
newString = ""
compareToPrevious = ""
for letter in userString:
    if len(newString) == 0:
        newString += letter
        compareToPrevious = letter
    if letter == compareToPrevious:
        continue
    else:
        newString += letter
        compareToPrevious = letter

print(newString)