# 🌟 Exercise 1: Cats
# Instructions
# Using this class
from functools import reduce
class Cat:

    cat_list = []
    def __init__(self, cat_name, cat_age):
        
        self.name = cat_name
        self.age = cat_age
        Cat.cat_list.append(self)
        
        

# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”.
# Use the function previously created.

snowball = Cat('Snowball', 1)
catnip = Cat('Catnip', 2)
funtik = Cat('Funtik', 3)


oldest_cat = reduce(lambda cat1, cat2: cat1 if cat1.age > cat2.age else cat2, Cat.cat_list)
print(f"The oldest cat is {oldest_cat.name} and it's {oldest_cat.age} years old")


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    dog_list = []
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height
        Dog.dog_list.append(self)

    def bark(self):
        print(f"{self.name} goes WOOF!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height*2}cm high!")

davids_dog = Dog('Rex', 50)

print(f"{davids_dog.name}, {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(f"{sarahs_dog.name}, {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

largest_dog = reduce(lambda dog1, dog2: dog1 if dog1.height > dog2.height else dog2, Dog.dog_list)
print(largest_dog.name)

# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
# Then, call the sing_me_a_song method. The output should be:
class Song:
    def __init__(self, lyrics: list):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

stairway = Song(lyrics = ["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Create a method called get_groups that prints the animal/animals inside each group.
# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.

class Zoo:
    def __init__(self, zoo_name: str) -> None:
        self.animals = []
        self.sorted_animals = {}
        self.name = zoo_name

    def add_animal (self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals (self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals (self):
        self.animals = sorted(self.animals)
        self.sorted_animals[0] = [self.animals[0]]
        for index in range(1, len(self.animals)):
            if self.animals[index][0] == self.animals[index-1][0]:
                self.sorted_animals[index-1].append(self.animals[index])
            else:
                self.sorted_animals[index] = [self.animals[index]]
            
            
        print(self.sorted_animals)
        
            


ramat_gan_safari = Zoo('Ramat Gan Safari')

ramat_gan_safari.add_animal('Hippo')
ramat_gan_safari.add_animal('Parrot')
ramat_gan_safari.add_animal('Ddd')
ramat_gan_safari.add_animal('Dog')

ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()


