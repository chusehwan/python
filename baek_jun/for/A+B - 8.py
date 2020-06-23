a = input()
a = int(a)

for i in range(a):
    b = input()
    c, d = b.split()
    p = 'Case #'+str(i+1)+': '+str(c) + ' + ' + str(d)+' = '+str(int(c)+int(d))
    print(p)