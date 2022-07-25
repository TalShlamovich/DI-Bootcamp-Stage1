# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator.
# We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# Download this word list
# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection.
# What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length.
# The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20.
# Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
from random import randint

def get_words_from_file(file):
    with open(file, mode = 'r') as f:
        word_list = []
        for word in f:
            word_list +=word.split()
        return word_list

# print(get_words_from_file(r'C:\Users\talsh\OneDrive\OneDrive Documents\Developers-Institute\DI-Bootcamp-Stage1\Week-5\Day-4\Exercises\sowpods.txt'))

def get_random_sentence(length):
    words_list = get_words_from_file(r'C:\Users\talsh\OneDrive\OneDrive Documents\Developers-Institute\DI-Bootcamp-Stage1\Week-5\Day-4\Exercises\sowpods.txt')
    generated_sentence = ''
    the_length = 0
    while the_length < length:
        index = words_list[randint(0, len(words_list)-1)]
        generated_sentence += ' ' + index
        the_length += 1
    return generated_sentence

# print(get_random_sentence(10))


def main():
    print("This function takes random words from txt file, converts them to lowercase and puts them in one string")
    user_length = int(input('How many words?: '))
    if 2 <= user_length <= 20:
         random_sentence = str(get_random_sentence(user_length)).lower()
         print(random_sentence)
    else:
        print('Sorry, the sentence must be betweet 2 and 20 words long')

# main()

# Exercise 2: Working With JSON
# Instructions

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

data = json.loads(sampleJson)
salary = data['company']['employee']['payable']['salary']
data['company']['employee']['birthdate'] = '12.09.1992'

with open('DI-Bootcamp-Stage1\Week-5\Day-4\Exercises\exercise.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)






