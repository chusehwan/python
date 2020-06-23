a = input()
a = a.split()
for i in range(len(a)):
    a[i]=int(a[i])

a.sort(reverse= True)
print(a[1])
