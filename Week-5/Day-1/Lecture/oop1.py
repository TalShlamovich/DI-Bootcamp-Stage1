from audioop import ratecv
import random


class Car: 
    def __init__(self) -> None:
        pass

class RPG_CHARACTER:
    """Class for RPG character creation"""
    characters_created = 0
    characters = {}

    def __init__(self, name:str, race: str, char_class: str) -> None:
        self.name = name
        self.level = 0
        self.xp = 0
        self.xp_next_level = 100
        self.race = race
        self.char_class= char_class
        # print(f"RPG CHARACTER initialised: name - {self.name}, race - {race}, class - {char_class}")
        RPG_CHARACTER.characters_created +=1
        RPG_CHARACTER.characters[self.name] = self

    def move (self):
        print (self.name + ' moves')

    def level_up(self):
        self.level += 1

    def set_next_levelXP(self):
        self.xp_next_level += self.level * self.xp_next_level
    
    def check_XP(self):
        if self.xp >= self.xp_next_level:
            self.level_up()
            self.set_next_levelXP()
            print(f"{self.name} has leveled up!")
        else: 
            pass

    def strike (self):
        self.xp +=5
        self.check_XP()
        print (self.name + " strikes")


    def block (self):
        print(self.name + " blocks")
        self.xp+=2
        self.check_XP()


conan = RPG_CHARACTER(name = 'Conan', race = 'Human', char_class='Warrior')
print(conan.level)

zena = RPG_CHARACTER('Zena', 'human', 'amazon')

# RPG_CHARACTER.move(conan)
# zena.strike()


def main():
    choices = ['strike', 'defence', 'move']   
    conan = RPG_CHARACTER(name = 'Conan', race = 'Human', char_class='Warrior')

    while conan.level < 3:
        action = random.choice(choices)
        if action == 'strike':
            conan.strike()
        if action == 'move':
            conan.move()
        if action == 'defence':
            conan.block()
        

main()

        