import math

# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

class Circle:
    def __init__(self, radius = 1.0) -> None:
        self.radius = radius

    def perimeter(self):
        perimiter = 2 * math.pi * self.radius
        return perimiter
    
    def area(self):
        area = math.pi * (self.radius**2)
        return area

    def definition():
        print("A circel is the set of all points in the plane that are a fixed distance (the radius) from a fixed point (the center)")


# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist.
# The list should be constructed with random numbers. (use list comprehension).

class MyList:
    def __init__(self, letters:list) -> None:
        self.letters = letters
    
    def reverse(self):
        self.letters.reverse()
    
    def sort(self):
        self.letters.sort()

something = MyList(['a', 'c', 'r', 'h', 'n'])

something.reverse()
print(something.letters)
something.sort()
print(something.letters)