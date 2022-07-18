import random
from xmlrpc.client import boolean
from ExercisesXP import Dog

# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

class PetDog(Dog):

    def __init__(self, name: str, age: int, weight: int) -> None:
        super().__init__(name, age, weight)
        self.trained = False
        
    
    def train (self):
        print(self.bark())
        self.trained = True
        print(self.trained)
        return self.trained
        

    def play(self, *args):
        output = f"{self.name}"
        for arg in args:
            output += f", {arg.name}"
        print(f"{output} play together")

    def do_a_trick(self):
        sentence1 = f"{self.name} does a barrel roll"
        sentence2 = f"{self.name} stands on his back legs"
        sentence3 = f"{self.name} shakes your hand"
        sentence4 = f"{self.name} plays dead"
        print(self.trained)

        phrases = [sentence1, sentence2, sentence3, sentence4]

        if self.trained == True:
            print(random.choice(phrases))
        else:
            print("Dog doesn't know any tricks")

            

dog1 = PetDog("dog1", 1, 10)
dog2 = PetDog('dog2', 2, 20)
dog3 = PetDog('dog3', 3, 30)

dog1.train()
dog1.do_a_trick()