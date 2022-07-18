# 🌟 Exercise 1 : Pets
# Instructions

# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese (Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat1 = Siamese("cat1", 1)
cat2 = Chartreux("cat2", 2)
cat3 = Bengal("cat3", 3)

all_cats = [cat1, cat2, cat3]
print(all_cats)

sara_pets = Pets(all_cats)

sara_pets.walk()


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog.
# This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name: str, age: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self) -> str:
        return f"{self.name} is barking"
    
    def run_speed(self) -> int:
        speed = self.weight/self.age*10
        return speed

    def fight(other_dog, self) ->str:
        other_dog.factor = other_dog.run_speed() * other_dog.weight
        self.factor = self.run_speed() * self.weight
        if other_dog.factor > self.factor:
            print(other_dog.name)
            return other_dog.name
        else:
            print(self.name)
            return self.name


dog1 = Dog("dog1", 1, 10)
dog2 = Dog('dog2', 2, 20)
dog3 = Dog('dog3', 3, 30)

# dog3.fight(dog1)
        




