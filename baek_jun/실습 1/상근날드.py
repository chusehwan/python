amount = []
aaa = []
for i in range(3):
    a = input()
    a = int(a)
    amount.append(a)
for i in range(2):
    a = input()
    a = int(a)
    aaa.append(a)

combined_list = []
for i in range(3):
    for y in range(2):
        set_price = amount[i]+aaa[y]-50
        combined_list.append(set_price)
print(min(combined_list))

