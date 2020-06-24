#Movie Tickets

while True:
    age = input('ple let me know your age : ')
    age = int(age)
    if age<3:
        print('cost is free')
    elif age>=3 and age<12:
        print('cost is $10')
    else :
        print('cost is $15')