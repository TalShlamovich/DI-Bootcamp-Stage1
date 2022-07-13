def calculation(x, y):
    addition = x + y
    substraction1 = x - y
    substraction2 = y - x
    return addition, substraction1, substraction2

# results = calculation(5, 10)
# print(results)
# print(type(results))


def calculation(x: int, y: int) -> tuple:
    addition = x + y
    substraction1 = x - y
    substraction2 = y - x
    return addition, substraction1, substraction2

# results = calculation(5, 10)
# print(results)
# print(type(results))


def welcome_statement(name: str, gender: str):
    if gender == 'M':
        return f"Hello Mr.{name}"
    if gender == 'F':
        return f"Hello Ms.{name}"

# TYPING
def allowed (accounts: list, restricted: list) -> list:
    """method for finding allowed profiles in a list"""
    allowed_list = []
    for account in accounts:
        if account not in restricted:
            allowed_list.append(account)
    return allowed_list


# *args - arguments .TUPLES * specifies that amount of args is not specified

def print_names(*names: tuple) -> None:
    for name in names:
        print(name)

print_names('Johnny','Franky', 'Steve', 'Stephen', 'Peter')

def return_args (*args) -> list:
    args_list = []
    for arg in args:
        args_list.append(arg)
    return args_list

result = return_args(1,2,3,'abc','kjh',[12,34])
# print(result)

# **kwargs = key value argument. KEY-VALUE PAIRS

def create_dict_func (**details):
    return details

details = create_dict_func(name='Yossi', address='Tel-Aviv', country='Israel')
# print(details)


def make_details (*names: tuple, **details: dict):
    full_details = {}

    for name in names:
        full_details[name] = details
    return full_details

f_details = make_details('Yossi', 'Lise', 'Reuven', Address = '', ZIP = -1, Phone = -1)
print(f_details)