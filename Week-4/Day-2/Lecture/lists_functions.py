a = []

# adding items
a.append(1)
a.append(1)
print(a)

# insert
a.insert(0, 0) #index, item
print(a)

# remove
a.remove(1) #the first occurence of this item
print(a)

# delete from memory
del a[0] #index

# pop removes from list but keeps in memory and returns it

#sorting
char_list = ['z', 'e', 'r', 'a', 'g']
sorted_char_list = sorted(char_list) #does not change the original list
print(sorted_char_list)

char_list.sort() #changes the list
print(char_list)

list1 = [5, 10, 15, 20, 25, 50, 20]

index_20 = list1.index(20)

list1.remove(20)
list1.insert(3, 200)

print(list1)


