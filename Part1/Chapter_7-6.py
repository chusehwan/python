#Three Exits


toppings=[]
print('pls input what you want to top')
print('if you want to stop, pls type"quit"')
flag = True
while flag:
    topping = input('topping :')
    if topping == 'quit':
        flag=False
    else:
        toppings.append(topping)
print(toppings)

