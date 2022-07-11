a_set = {1, 2, 3, 4} #with no values it is considered to be a dictiobnary

duplicates_list = [1,1,1,1,2,2,'a','c']

list_to_set = set(duplicates_list)
print(list_to_set) 

#does not allow duplicates
# cannot use indexes

colour_a = {'red', 'green', 'blue', 'yellow'}
colour_b = {'brown', 'green', 'pink', 'black'}

#Intersection  which values exist in both sets
print("Intersection:", colour_a & colour_b)

#Union
print("Union:", colour_a | colour_b)

#Without Intersection
print("without interesection:", colour_a ^ colour_b)

#Difference
print("Difference a - b:", colour_a - colour_b)
print("Difference b - a:", colour_b - colour_a)

#addition
colour_a.add('purple')
print(colour_a)