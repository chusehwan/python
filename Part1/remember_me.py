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
    if username:
        print("Welcome back, "+username +"!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, "+ username +"!")

greet_user()
