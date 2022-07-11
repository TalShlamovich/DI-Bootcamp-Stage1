list = [1, 2, 3, 4, 5]
#index looping. better for looping in specific indexes
for i in range(len(list)):
    print(i)

#looping through the items themselves
for i in list:
    print(i)

# better for everything else (you want to loop from the start)
for i, val in enumerate(list):
    print(i)
    print(val)

product = list[0]
for number in list[1:len(list)]:
    product *= number
print(product) 