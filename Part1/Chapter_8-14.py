#Cars

def make_car(manufacturer, model,**moreinfo):
    car_lists={}
    car_lists['manufacturer']=manufacturer
    car_lists['model']=model
    for k,v in moreinfo.items():
        car_lists[k]=v
    return car_lists


car = make_car('subaru','outback',color='blue',tow='True')
print(car)