# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message (subject: str) -> str:
    return f"I am learning {subject}"

answer = display_message("Python")
print(answer)

# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favourite_book(title: str) -> str:
    return print(f"One of my favourite books is {title}")

favourite_book("Martin Eden")

# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city: str, country: str) -> str:
    return print(f"{city} in in {country}")

describe_city("Belfast", "the UK")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 
# and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message,
# otherwise show a fail message and display both numbers.
import random
# user_number = input("Guess which number I have in mind (1-100): ")
# user_number = int(user_number)

def compare_numbers (user_number: int) -> None:
    generated_number = random.randint (1, 100)
    if user_number == generated_number:
        return print("Congratulations, you guessed correctly!")
    else:
        return print(f"Sorry, you guessed {user_number} instead of {generated_number}")

# compare_numbers(user_number)


# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

def make_shirt_simple (size: str, message: str) -> None:
    return print(f"The size of the shirt is {size} and the text is '{message}'")

# make_shirt_simple("L", "Hello")

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

def make_shirt_lvl2 (size: str = "L", message: str = "I love Python") -> None:
    return print(f"The size of the shirt is {size} and the text is '{message}'")

make_shirt_lvl2()
make_shirt_lvl2("M")
make_shirt_lvl2("M", "Python loves you")

# Bonus: Call the function make_shirt() using keyword arguments.

make_shirt_simple(message="hi", size = "S")


# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names. 

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

def show_magicians(names: list) -> str:
    for name in names:
        print(name)
        

# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.

the_great = " the Great"
def make_great(names: list):
    for index, name in enumerate(names):
        names[index] += the_great
    return [names]

# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

make_great(magician_names)
print(magician_names)
show_magicians(magician_names)


# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
# print(get_random_temp())
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season,
# eg. if season is ‘winter’,temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

# season = input("Name a season: ")
# season = season.lower()

season = input("Give me a number of a month: ")
season = int(season)


def get_random_temp(season: str) -> int:
    # if season == "winter":
    if season == 1 or season == 2 or season == 12:
        return random.uniform (-10, 10)

    # elif season == "spring":
    elif 3 <= season <= 5:
        return random.uniform (10, 25)

    # elif season == "summer":
    elif 6 <= season <= 8:
        return random.uniform (30, 40)

    # elif season == "autumn" or season == "fall":
    elif 9 <= season <= 11:
        return random.uniform (5, 20)
    

def main (season) -> None:

    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")

    elif temperature < 16:
        print("Quite chilly! Don’t forget your coat")

    elif 16 <= temperature <= 23:
        print("A light jacket should suffice.")

    elif 24 <= temperature <= 32:
        print("Don't forget you sunscreen.")

    else:
        print("Just stay inside with AC on.")

main(season)