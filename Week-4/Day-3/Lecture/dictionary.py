user_a = {
    'firstName': 'Bob',
    'lastName': 'Ross',
    'age': 53,
    'address': 'Tel-Aviv',
    'family': [('Jessica', 34), ('Tommy', 8)]
}

print(user_a['firstName'])
print(user_a.keys())

for key in user_a.keys():
    print("KEys: ",key)

for value in user_a.values():
    print("Value:", value)  

for key, value in user_a.items():
    print("Key and Value: ", (key, value))

#can use pop and del



sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

history = sample_dict["class"]["student"]["marks"]["history"]


sample_dict1 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

del sample_dict1['name']
del sample_dict1['salary']
print(sample_dict1)