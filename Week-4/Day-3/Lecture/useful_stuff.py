list_a = ['Yossi', 'Lise', 'Avner']
list_b = [1991, 1992, 1993]
list_c = ['Tel-Aviv', 'Ramat Gan', 'Givatayim']
# COMBINING MORE THAN 2 LISTS INTO OBJECTS
members = list(zip(list_a, list_b, list_c))
# print(members)
info_data = []
for user in members:
    user_dict = {
        'name' : user[0],
        'year' : user[1],
        'residence': user[2]
    }
    info_data.append(user_dict)
print(info_data)

# LIST COMPREHENSION. way to create a list in a dynamic and fast way

squared_num = []

for n in range(5,10):
    if n % 2 == 0:
        squared_num.append(n)
        continue
    squared_num.append(n**2)
print(squared_num)

# what kind value to store? From where?(where is n from) 
# just don't do it when you have a lot of conditions. It is VERY CONFUSING
squared_num = [n**2 for n in range(5,10)]
print(squared_num)

squared_num = [n**2 if n % 2 !=0 else n for n in range(5,10)]
print(squared_num)

# DICTIONARY COMPREHENSION
# key and value. where does it come from
dictionary_comp = {key: value for key, value in enumerate('ABC')}
print(dictionary_comp)