# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)


# Implement the following methods:
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family:
    def __init__(self, memebers: list[dict], last_name:str) -> object:
        self.members = memebers
        self.last_name = last_name
    
    
    def born(self:object, **baby) -> None:
        
        self.members.append(baby)
        print(f"Congratulation for {baby['name']}'s birth")

    def is_18(self, name) -> None:
       for member in self.members:
            if name in member['name']:
                if member['age'] >= 18:
                    print("18 or over")
                    return True
                else: 
                    print("Not old enough")
                    return False
                

    def family_presentation(self) -> str:
        sentence = f"{self.last_name}"
        for member in self.members:
            sentence += f"\n{member['name']}"
        print(sentence)
        return sentence




ivanov = Family([
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
], 'Ivanov')

ivanov.born(name = 'Lisa', age = 20, gender = 'Female', is_child = True)
ivanov.is_18('Lisa')
ivanov.family_presentation()



# class TheIncredibles(Family):
    
#     def use_power(self, name:str):
#        if self.is_18(name):
            




# incredible = [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]

# incredible_fam = TheIncredibles(incredible, 'Incredible')