from collections import namedtuple
from time import sleep
import random
import pprint


Traits = namedtuple("Traits", 'strength intelligence dexterity character_class defence')
pp = pprint.PrettyPrinter(indent=4)


class CharacterTraits:

    def __init__(self, strength:int, intelligence:int, dexterity:int, character_class:str, defence:str):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.character_class = character_class
        self.defence = defence


class RPG_CHARACTER:
    """Class for creating RPG character"""
    characters_created = 0
    characters = {}
    def __init__(self, name:str, traits = Traits(0,0,0,'None',0)) -> object:
        self.name = name

        self.level = 1
        self.xp = 0 
        self.xp_next_level = 100

        self.traits = CharacterTraits(*traits)

        RPG_CHARACTER.characters_created += 1
        RPG_CHARACTER.characters[self.name] = self

    def move(self) -> None:
        print(self.name + ' moves')

    def level_up(self):
        self.level += 1
    
    def set_next_levelXP(self):
        self.xp_next_level += self.level * self.xp_next_level

    def checkXP(self):
        if self.xp >= self.xp_next_level:
            self.level_up()
            self.set_next_levelXP()
            print(f"{self.name} is Leveled UP! Now level is {self.level}")
        else:
            pass

    def strike(self) -> None:
        print(self.name + ' Is striking')
        self.xp += 5
        self.checkXP()
            
    def defence(self) -> None:
        print(self.name + ' Is defending')
        self.xp += 2
        self.checkXP()

    def print_characters():     
        pp.pprint(RPG_CHARACTER.characters)

