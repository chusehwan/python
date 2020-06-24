import json

filename = 'json_sample.json'
with open(filename,'r') as f_obj:
    numbers =json.load(f_obj)

print(numbers)