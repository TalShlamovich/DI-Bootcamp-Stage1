# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

word = input('Give me a word: ')

wordDictionary = {}

for index in range(len(word)):
    if word[index] not in wordDictionary:
        wordDictionary[word[index]] = [index]
    else:
        wordDictionary[word[index]].append(index)
print(wordDictionary)

# for i, char in enumerate(word)

#     if char in wordDictionary:
#         wordDictionary[char].append(i)
#         continue
#     wordDictionary[char] = [i]

# print(wordDictionary)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

item_purchase = {
    'TV': 100,
    'stereo': 50,
    'PC': 90,
    'macbook': 1000
}

wallet = 200
output = []

for key, value in enumerate(item_purchase):
    # print(item_purchase[value])

    if item_purchase[value] <= wallet:
        output.append(value)

print(output)

# So initially I did not notice that there are $ signs and commas
# and made mine without them

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
wallet_clean = int(wallet.strip('$'))

can_afford = []
for product, price in items_purchase.items():
    
    price_split = price.split(',')
    price_joined = "".join(price_split)
    price_clean = int(price_joined.strip('$'))
    
    if price_clean > wallet_clean:
        continue
    can_afford.append(product)
print(can_afford)
    