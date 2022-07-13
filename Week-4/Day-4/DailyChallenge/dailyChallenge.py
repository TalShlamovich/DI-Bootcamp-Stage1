matrix = [
    ['7','T','h','i','s','$','#','^'],
    ['i','s','%',' ','M','a','t','r'],
    ['3','i','x','#',' ',' ','%','!']
]
message = ""
prev_char = ''
current_char = ''
for index, line in enumerate(matrix):
    # print(index, line)
    for i, character in enumerate(matrix[index]):
        current_char = character
        # print(type(character))
        if character.isalpha():
            prev_char = character
            message += current_char
        elif character.isdigit():
            continue
        else:
            message += " "

        if message[i-1] == " ":
            continue
            

print(message)