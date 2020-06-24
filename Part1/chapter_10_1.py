with open('learning_python.txt') as learntest:
    learn = learntest.readlines()
    a=0
    test = ''
    for le in learn:
        print(le.strip())
        a+=1
        if a>2:
            break
    for le in learn:
        print(le.strip())
        test +=le.rstrip()

print(test)

print(test.replace('python','C'))
print(test)


