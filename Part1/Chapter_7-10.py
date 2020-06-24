#Dream Vacation

dream_vacation = {}

active_flag= True

print('If you could visit one place in the world'
      ' where would you go?')
print('if you want to stop, pls type "quit".')

while active_flag:

    name = input('your name : ')
    place = input('dream place :')
    flagp = input('if you want to stop, type "quit"')
    dream_vacation[name]=place
    if flagp=='quit':
        active_flag = False



for k,v in dream_vacation.items():
    print(k +"'s dream vacation is :" + v)

