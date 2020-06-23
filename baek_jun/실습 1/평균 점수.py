test_score =[]
for i in range(5):
    a = input()
    a=int(a)
    if a<40:
        a=40
    test_score.append(a)

print(int(sum(test_score)/len(test_score)))


