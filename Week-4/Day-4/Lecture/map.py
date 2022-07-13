numbers = [1,2,3,4,5]

to_power = lambda n, power: n**power

def set_power(power):
    return lambda n: n ** power

p2_lambda = set_power(3)


result = list(map(lambda n: n**2, numbers))
result = list(map(p2_lambda, numbers))
# print(result)

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# def four_letters(name):
#     return len(name) == 4

# def say_hello(name):
    
#     return (f"Hello, {name}")

# filtered_list = list(filter(four_letters, people))
# print(filtered_list)


# hello = str(map(say_hello, filtered_list))
# print(hello)

