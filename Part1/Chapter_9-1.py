class Restaurant():
    def __init__(self, rest_name, cusine_type):
        self.name = rest_name
        self.type = cusine_type

    def des_restaurant(self):
        print(self.name + ' is name! and type : '+self.type)

    def open_restaurant(self):
        print('restaurant is open')

my_res = Restaurant('outback','family')

my_res.des_restaurant()
my_res.open_restaurant()