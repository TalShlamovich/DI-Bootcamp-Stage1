user_input = input("Write a few words separated by a comma (,): ")

result = ",".join(sorted(user_input.split(',')))

print(result)