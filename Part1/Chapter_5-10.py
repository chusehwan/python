current_users = ['a','b','c','d','f','e','admin']
new_users = ['d','e','F','g',]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ' is already in current_users')
    else:
        print('add new_user ' + new_user)
