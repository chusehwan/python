#pizzas

pizza_list = ['pizza_a','pizza_B','pizza_C']

for pizza in pizza_list:
    print('you like '+ pizza +'!')
    print('you like pizza very much!')

print('Thanks you!')

pizza_list.append('added_pizza')
print(pizza_list)
friend_pizza = pizza_list[:]
friend_pizza.append('second_added_pizza')
print('my favorite pizza : ' + str(friend_pizza))

for pizza in friend_pizza:
    print(pizza)