# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

def absolute(value):
    """--abs() method returns the absolute value of the given number--"""
    absolute_value = abs(value)
    return absolute_value
    

# print(absolute.__doc__)
# print(absolute(-4.5))

def integer(value):
    """converts any string, bytes-like object or a number to integer and returns it"""
    pass

# print(integer.__doc__)

def theInput(value):
    """Takes input from a user and converts it to a string"""
    pass

# print(theInput.__doc__)


# 🌟 Exercise 2: Currencies
# Instructions

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        

    def __str__(self):
        output = f"{self.amount} {self.currency}s"
        print(output)
        return output

    def __int__(self):
        print(self.amount)
        return self.amount

    def __repr__(self):
        return str(self)

    def __add__(self, num):
        if type(num) == int:
            sum = int(self) + num
            print(sum)
            return sum
        elif self.currency == num.currency:
            sum = int(self) + int(num)
        else:
            raise Exception("off")

    def __call__(self):
        
        return str(self)

    def __iadd__(self, num):
        self.amount += int(num)
        print(self.amount)
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# str(c1)
# int(c1)
# repr(c1)
c1 + 5
# c1 + c2
# c1()
# c1 +=5
# c1()
# c1 += c2
# c1()
c1+c3