#my own solution

# matrix = [
#     ['7', 'T', 'h', 'i', 's', '$', '#', '^'],
#     ['i', 's', '%', ' ', 'M', 'a', 't', 'r'],
#     ['3', 'i', 'x', '#', ' ', ' ', '%', '!']
# ]



# message = ""
# is_prevchar = False
# current_char = ""
# for l in matrix:

#     for character in l:
#         if character.isdigit():
#             continue
#         elif character.isalpha():
#             is_prevchar = True
#             message +=character
#         if is_prevchar and not character.isalpha():
#             message +=" "
#             is_prevchar = False

# print(message)

# Solved a bit differently in class
mat = """
    7i3
    Tsi
    h%x
    i #
    sM 
    $a 
    #t%
    ^r!
    """

mat_modified = mat.split('    ')
print(mat_modified)

for idx, word in enumerate(mat_modified):
    mat_modified[idx] = word.strip('\n')
print(mat_modified)

del mat_modified[0]
del mat_modified[-1]
print(mat_modified)
mat_modified = [list(chars) for chars in mat_modified]
print(mat_modified)
col1, col2, col3 = zip(*mat_modified)
print(col1)
print(col2)
print(col3)

message = ''
#  * unpacks items from tuple list
for l in (*col1, *col2, *col3):
    if l.isdigit():
        continue
    elif l.isalpha():
        message += l
    else:
        if message[-1] == ' ':
            continue
        message += ' '
print(message)