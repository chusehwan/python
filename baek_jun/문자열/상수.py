a = input()
a = a.split()
a_1 = a[0]
a_2 = a[1]
r_a_1 = ''
r_a_2 = ''
for i in range(len(a_1)):
    i = (i+1)*-1
    r_a_1 = r_a_1 + a_1[i]

for i in range(len(a_2)):
    i = (i+1)*-1
    r_a_2 = r_a_2 + a_2[i]

if r_a_1 > r_a_2:
    print(r_a_1)
else:
    print(r_a_2)
