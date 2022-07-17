class Farm: 
    def __init__(self, name) -> None:
        self.animals = {}
        self.animal_types = []
        self.string_animals = ''
        self.name = name

    def add_animal(self, animal, quantity = 1):
        if animal not in self.animals:
            self.animals[animal] = quantity
        else:
            self.animals[animal] += quantity

    def get_info(self):
        print(f"{self.name}'s Farm \n{self.animals} \nE-I-E-I-0!")

    def get_animal_types(self):
        self.animal_types = sorted(list(self.animals.keys()))
        print(self.animal_types)
        return self.animal_types

    def get_short_info(self):
        self.string_animals = ', '.join(self.get_animal_types())
        print(f"{self.name}'s farm has {self.string_animals}")

        

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# macdonald.get_animal_types()
macdonald.get_short_info()