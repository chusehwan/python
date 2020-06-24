from typing import List

guest_list=['guest1','guset2','guest3','guest4','guset5']

message = 'Dear ' + guest_list[0] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[1] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[2] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[3] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[4] + '! I invite you on my dinner Party!'
print(message)
print(len(guest_list))

print(guest_list[0] + ' Cant coming my party')

guest_list[0]='NewGuest'
print('New Guest list is \n' + str(guest_list))

message = 'Dear ' + guest_list[0] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[1] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[2] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[3] + '! I invite you on my dinner Party!'
print(message)
message = 'Dear ' + guest_list[4] + '! I invite you on my dinner Party!'
print(message)

guest_list.insert(0,'first_insert_guest')
print(guest_list)
guest_list.insert(3,'middle_insert_guest')
print(guest_list)
guest_list.append('last_insert_guest')
print(guest_list)

print("sorry for inconvience, i can invite only 2 person")

sorry = guest_list.pop()
print('Dear ' + sorry + ',i appoligy for un invite you ')
sorry = guest_list.pop()
print('Dear ' + sorry + ',i appoligy for un invite you ')
sorry = guest_list.pop()
print('Dear ' + sorry + ',i appoligy for un invite you ')
sorry = guest_list.pop()
print('Dear ' + sorry + ',i appoligy for un invite you ')
sorry = guest_list.pop()
print('Dear ' + sorry + ',i appoligy for un invite you ')
sorry = guest_list.pop()
print('Dear ' + sorry + ',i appoligy for un invite you ')

print(guest_list)

print(guest_list[0] + ", You're still on my invite list")
print(guest_list[1] + ", You're still on my invite list")

del(guest_list[1])
del(guest_list[0])
print(guest_list)