
while True:
    try:
        a = input()
        a = a.split()
        print(int(a[0])+int(a[1]))
    except:
        break