#Programming Poll

answers=''
a=1
while True:
    answer = input('Why do you like programming ?: \n')
    if answer == 'q':
        break
    answers+=str(a) +'. '+ answer +'\n'
    a+=1

with open('10_5.txt','w') as abc:
    abc.write(answers)

