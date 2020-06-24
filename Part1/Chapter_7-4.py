#Pizza Toppings

toppings=[]
print('pls input what you want to top')
print('if you want to stop, pls type"quit"')
while True:
    topping = input('topping :')
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
print(toppings)

