# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {1, 2, 3}

# Add two new numbers to the set.
my_fav_numbers.add(4)
my_fav_numbers.add(5)

# Remove the last number.
my_fav_numbers.remove(5)

# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {6, 7, 8, 9}

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# tuples are immutable, so no, you cannot add anything to a tuple unless in the end you create another tuple.

# 🌟 Exercise 3: List
# Instructions
# Using this list;
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove “Banana” from the list.
basket.remove("Banana")

# Remove “Blueberries” from the list.
basket.remove("Blueberries")

# Add “Kiwi” to the end of the list.
basket.append("Kiwi")

# Add “Apples” to the beginning of the list.
basket.insert(0, "Apples")

# Count how many apples are in the basket.
basket.count("Apples")

# Empty the basket.
basket.clear()

# Print(basket)
print(basket)

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Float is a number with a decimal point. Ineger is a number without a decimal point.
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

listFloats = []
for i in range(3, 11, 1):
    listFloats.append(i/2)
print(listFloats)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
allNumbers = ''
for i in range(1,21,1):
    print(i)

# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for index, value in enumerate(range(1,21,1)):
    if index%2 == 0:
        print(value)


# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
userName = input("What is your name?")
while userName != "Tal":
    userName = input("What is your name?")

# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
userFruits = input("What are your favourite fruits? please separate them with space: ")

# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
listFruits = list(userFruits.split(" "))

# Now that we have a list of fruits, ask the user to input a name of any fruit.
anyFruit = input("Now give me any fruit (can be from the list as well): ")

# If the user’s input is in the favorite fruits
#  list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
if anyFruit in listFruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
toppings = ''
price = 10
userToppings = input("What would you like to add to your pizza? type 'quit' to go to checkout")
while userToppings != 'quit':
    toppings += (f'{userToppings} ')
    price += 2.5
    print("The topping is added!")
    userToppings = input("What would you like to add to your pizza? type 'quit' to go to checkout")
else:
    print(f"You chose the following toppings:\n{toppings}")
    print(f'Your total is ${price}')
    

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

ages = input("What are the ages of each person that wants a ticket? ")
agesList = list(ages.split(", "))
agesList = list(map(int, agesList))

total = 0
for age in agesList:
    if age<3:
        total += 0
    elif age >= 3 and age <= 12:
        total += 10
    else:
        total += 15
print(f'Your total is ${total}')



# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks a teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

namesList = ['David', 'Shaul', 'Frank']
teenAge = input("What are the ages of David, Shaul and Frank?: ")
teenAgeList = list(teenAge.split(", "))
teenAgeList = list(map(int, teenAgeList))
print(teenAgeList)

for i in teenAgeList:
    if i < 16 or i > 21:
        # print(i)
        del namesList[teenAgeList.index(i)]
print(namesList)


# Exercise 10 : Sandwich Orders
# Instructions
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.