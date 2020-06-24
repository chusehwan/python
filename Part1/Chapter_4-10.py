#Slices

random_list = ['a','b','c','d','e','f','g']
print('first three items are : '+str(random_list[:3]))

for value in random_list[:3]:
    print('first three items are :'+value)

print('\n')

for value in random_list[3:6]:
    print('middle three items are :'+value)
print('\n')
for value in random_list[-3:]:
    print('last three items are :' + value)
