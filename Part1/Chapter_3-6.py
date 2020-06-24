from typing import List

guest_list: List[str]=['guest1','guset2','guest3','guest4','guset5']

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