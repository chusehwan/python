#No Pastrami

#Deli

sandwich_orders=['pastrami','pastrami','pastrami','sandwich_A','sandwich_B','sandwich_C','sandwich_D','sandwich_E']
finished_sandwich =[]

if 'pastrami' in sandwich_orders:
    print('sorry, pastrami rus out')
    
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finish = sandwich_orders.pop()
    finished_sandwich.append(finish)
    print('I made  your '+ finish)

for s in finished_sandwich:
    print(s + ' finished!')