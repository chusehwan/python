available_toppings = [ 'a','b','c','d','e','f']
requested_toppings = ['a','b','c','g']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('adding '+requested_topping +'.')
    else:
        print("sorry, we don't have "+requested_topping +'.' )
