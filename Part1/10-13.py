##Verify User

import json

def get_stored_username():
    """ Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename,'r') as f_obj:
            username =json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """prompt for a new username."""
    username = input('what is your name?')
    filename = 'username.json'
    with open (filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """greet the user by name"""
    username = get_stored_username()
    print("is your name " + username + " correct ?\n")
    answer = 'a'
    while answer != 'y' or answer != 'n':
        answer = input('pls put "y"/"n".')
        if answer == 'y':
            break
        elif answer == 'n':
            username = get_new_username()
            break

    if username:
        print("Welcome back, "+username +"!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, "+ username +"!")

greet_user()
