string = input().upper()
string_list = []
charactor_list = []
for i in range(len(string)):
    if string[i] not in string_list:
        string_list.append(string[i])

for i in range(len(string)):
    charactor_list.append(string[i])

num_list = []
for i in string_list:
        num_list.append(charactor_list.count(i))
# max num을 구하고 해당 max num이 1개인지 1개이상인지 판단


for i in range(len(num_list)):
    if num_list[i] == max(num_list):
        result = string_list[i]

a = num_list.count(max(num_list))
if a > 1:
    result = '?'

print(result)



