# Global scope
# username = input('Username: ')
# password = input('Password: ')

# valid_username = 'yossiA'
# valid_password = 'ABC123'

# if username == valid_username:
#     # Local scope
#     print("hello")
# else:
#     print("invalid username")
number = int(input("number from 1 to 100"))
if number % 3 == 0 and number % 5 !=0:
    print("fizz")
elif number % 5 == 0 and number % 3 !=0:
    print("buzz")
elif number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")   