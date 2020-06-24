#Favorite Number
import json

filename = 'favorite_number.json'

with open(filename,'r') as f_obj:
    favor_number = json.load(f_obj)
    print("I know your favorite number! It's : " + favor_number)