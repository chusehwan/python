a = input()
a = int(a)

for i in range(a):
    b = input()
    c, d = b.split()
    print('Case #'+str(i+1)+': '+str(int(c)+int(d)))