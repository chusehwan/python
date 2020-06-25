dials = {2:['A','B','C'], 3: ['D','E','F'], 4: ['G','H','I'], 5: ['J','K','L'], 6:['M','N','O'], 7:['P','Q','R','S'],
         8:['T','U','V'], 9:['W','X','Y','Z']}
# UNUCIC = 36
text = input()
#text = 'UNUCIC'
text_list = []
for i in range(len(text)):
    text_list.append(text[i])


key_list = list(dials.keys())
i = 0
result = 0
for a in text_list:
    for y in key_list:
        if a in dials[y]:
            result = result + int(y)+1

print(result)