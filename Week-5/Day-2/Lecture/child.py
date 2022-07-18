from collections import namedtuple
from time import sleep
import random
import pprint
from parent import RPG_CHARACTER

class Warrior(RPG_CHARACTER):
    def __init__(self, name: str, traits=...) -> object:
        super().__init__(name, traits)
        self.chara

class Mage(RPG_CHARACTER):
    pass

zina = RPG_CHARACTER("Zina", traits = (100, 150, 120, 'Warrior', 300))

# def main():
#     choices = ['strike', 'defence', 'move']    
#     conan = RPG_CHARACTER("Conan", traits = (100, 150, 120, 'Warrior', 300))

#     while conan.level < 3:
#         action = random.choice(choices)
#         if action == 'strike':
#             conan.strike()
#         if action == 'defence':
#             conan.defence()
#         if action == 'move':
#             conan.move()
#         sleep(0.1)

# main()

conan = Warrior()