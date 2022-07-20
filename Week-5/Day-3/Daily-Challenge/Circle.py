# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them
import turtle
class Circle:

    def __init__(self, radius: int) -> None:
        self.radius = radius
        self.diameter = radius * 2

    @classmethod
    def from_diameter(cls, diameter):
        new_circle =  Circle(diameter/2)
        return new_circle

    def area(self):
        return 3.14 * self.radius ** 2

    def print_circle(self):
        output = turtle.circle(self.area())
        return output

    def __add__(self, circle):
        return Circle(self.radius + circle.radius)

    def __le__(self, circle):
        return self.area() <= circle.area()

    def __eq__(self, circle):
        return self.area() == circle.area()

    def __lt__(self, circle): #for sorting
        return self.area() < circle.area

    # def __repr__(self):
    #     return str(self.area())

    

    
        

circle1= Circle(2)

print(f"Circle1: r-{circle1.radius} d-{circle1.diameter}")

circle2 = Circle.from_diameter(6)
print(f"Circle2: r-{circle2.radius} d-{circle2.diameter}")

# circle2.print_circle()

circle3 = circle1 + circle2

print(f"Circle3: r-{circle3.radius} d-{circle3.diameter}")

print(circle2 >= circle1)
print(circle2 == circle1)

circle_list = [circle3, circle2, circle1]
circle_list.sort()


