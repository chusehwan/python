#Guest Book
filename='guest_book.txt'
ffff = ''

while True:
    username = input('put your name : \n')
    if username == 'quit':
        break
    print('greeting ! :' + username + '\n')
    filebody = input('put your wish visit : \n')
    print('if you want to quit, pls put "quit".')
    if filebody == 'quit':
        break
    else:
        ffff+=username +"'s wish place is  : "+ filebody + '\n'


with open(filename,'w') as fbody:
    fbody.write(ffff)





