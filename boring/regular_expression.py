import re

phonenumregex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phonenumregex.search('my number is (415) 555-4242.')


batregex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batregex.search('Batmobile lost an wheel.')
print(mo.group())

