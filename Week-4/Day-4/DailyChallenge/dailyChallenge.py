matrix = [
    ['7', 'T', 'h', 'i', 's', '$', '#', '^'],
    ['i', 's', '%', ' ', 'M', 'a', 't', 'r'],
    ['3', 'i', 'x', '#', ' ', ' ', '%', '!']
]



message = ""
is_prevchar = False
current_char = ""
for l in matrix:

    for character in l:
        if character.isdigit():
            continue
        elif character.isalpha():
            is_prevchar = True
            message +=character
        if is_prevchar and not character.isalpha():
            message +=" "
            is_prevchar = False

print(message)