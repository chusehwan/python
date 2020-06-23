a = input()
a=int(a)

for i in range(a):
    print('*'*(i+1))
for i in range(a-1):
    print('*'*(a-1))
    a-=1

print('---')