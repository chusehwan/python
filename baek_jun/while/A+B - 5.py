
while True:
    a = input()
    a = a.split()
    if int(a[0]) == 0 and int(a[1])==0:
        break
    print(int(a[0])+int(a[1]))