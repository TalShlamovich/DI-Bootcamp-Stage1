# while True:    
#     try:
#         user_in = int(input("Number: "))
#         print(user_in, 'number !')
#         break

#     except ValueError:
#         print(f'Invalid Type!')
#         continue

# VALID_CHOICES = ['Quit', 'Start', 'X', 'O']


my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
sum = 0
for value in my_list:
    try:
        sum += value
    except:
        continue

print(sum)