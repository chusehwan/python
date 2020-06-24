#Ice Cream Stand

class Restaurant():
    def __init__(self, rest_name, cusine_type):
        self.name = rest_name
        self.type = cusine_type

    def des_restaurant(self):
        print(self.name + ' is name! and type : '+self.type)

    def open_restaurant(self):
        print('restaurant is open')

class IceCreamStand(Restaurant):
    def __init__(self,rest_name, cusine_type):
        super().__init__(rest_name,cusine_type)
        self.flavors = flavors['a','b','c','d',]
    def print_falvors(self):
        for flavor in self.flavors:
            print(flavor)


my_res = Restaurant('outback','family')

my_res.des_restaurant()
my_res.open_restaurant()
my_res.print_falvors()