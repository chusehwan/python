#Deli

sandwich_orders=['sandwich_A','sandwich_B','sandwich_C','sandwich_D','sandwich_E']
finished_sandwich =[]

while sandwich_orders:
    finish = sandwich_orders.pop()
    finished_sandwich.append(finish)
    print('I made  your '+ finish)

for s in finished_sandwich:
    print(s + ' finished!')