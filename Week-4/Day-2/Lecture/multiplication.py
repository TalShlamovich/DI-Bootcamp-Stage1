# userNumber = int(input("Give me a number from 1 to 9: "))

# for i in range(0, 11, 1):
#     print(f'{userNumber*i}')

for i in range (1, 5, 1):
    product = ""
    for j in range (0,11,1):
        product +=f'{i} times {j} is {i*j}\n'
    print(product)