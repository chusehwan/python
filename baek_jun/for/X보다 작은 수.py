a=input()
b=input()
a= a.split()
list = b.split()
N = a[0]
X = a[1]

for i in list:
    if int(i) < int(X):
        print(i)

