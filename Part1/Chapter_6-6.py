favorite_language = {
    'name_A':'language_A',
    'name_B': 'language_B',
    'name_C': 'language_C',
    'name_D': 'language_D',
    'name_E': 'language_E',
    }
target_people = ['name_A','name_B','name_G']

for person in target_people:
    if person in favorite_language.keys():
        print(person + ' thank you for respond.')
    else:
        print(person + ' pls take a poll.')