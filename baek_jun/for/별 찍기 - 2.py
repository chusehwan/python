a = input()
a = int(a)
vac_count = a-1
for i in range(a):
    star = vac_count*' '+'*'*(i+1)
    print(star)
    vac_count-=1