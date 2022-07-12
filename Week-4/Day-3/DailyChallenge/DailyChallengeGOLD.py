userInput = input("Give me a word: ").lower()
shift = input("Give me a number from 0 to 25: ")
shift = int(shift)
secretCode = ""

while shift < 0 or shift > 25:
    shift = input("Give me a number from 0 to 25: ")
    shift = int(shift)

for i in range(len(userInput)):
    letter = userInput[i]
    if letter == " ":
        secretCode += " "
    else:
        secretCode += chr((ord(letter) + shift - 97) % 26 + 97)

print(secretCode)