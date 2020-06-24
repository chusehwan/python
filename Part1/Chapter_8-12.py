#Sandwiches
def sand(*sandwichies):
    count = 0
    for s in sandwichies:
        if count > 2:
            break
        print('your '+str(count+1) +' sandwich '+s +' has been ordered')
        count +=1


sand('Sand_A','Sand_B','Sand_C','Sand_D','Sand_E')
