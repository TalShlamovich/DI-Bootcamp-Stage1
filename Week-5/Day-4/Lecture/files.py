# file_text = ''
# file_text_lines = []

# def read_file(file):
#     file_txt = ""
#     with open(file, mode='r') as f:
#         print(f.tell())
#         file_txt += f.read()
#         return file_txt   

# def write_to_file(file, input_str, pointer_idx=None):
#     original_text = read_file(file)

#     with open(file, mode='w') as f:
#         f.write(original_text)
#         if pointer_idx:
#             f.seek(pointer_idx)
#         f.write(input_str)
        
# write_to_file('./sample.txt', '!&@^#^@!#^!@', 70)

#STEP 1
f = open("sample.txt","r")
#STEP 2
lineList = f.readlines()
count = len(lineList)
#STEP 3
print(count)
input = int(input("display line number:")) - 1
print(lineList[input])
# STEP 4
f.close()

