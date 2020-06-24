filename='guest.txt'
filebody = input('put your name : \n')
while True:
    filebody = input('put your name : \n')
    print('greeting ! :' = filebody)


with open(filename,'w') as ctest:
    ctest.write(filebody)
