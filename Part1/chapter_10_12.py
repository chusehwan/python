#Favorite Number Remembered
import json

filename = 'favorite_number.json'

try:
    with open(filename,'r') as f_obj:
        favor_number = json.load(f_obj)
        print("I know your favorite number! It's : " + favor_number)
except:
    with open(filename,'w') as f_obj:
        favor_number = input("There're no file to open, pls put your favorite number : ")
        json.dump(favor_number, f_obj)
        print("I'll save your faovor number as : " + favor_number)