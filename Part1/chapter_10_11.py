#Favorite Number
import json

answer=str(input("what is your favorite number?"))
filename = 'favorite_number.json'

with open(filename,'w') as f_obj:
    json.dump(answer,f_obj)