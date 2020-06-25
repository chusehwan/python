text_list = []
for i in range(97, (97+26)):
    text_list.append(chr(i))
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text_list = text_list + cro_list
print(text_list)
# remove