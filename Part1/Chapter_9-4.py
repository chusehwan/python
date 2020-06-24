#Number Served

class Restaurant():
    def __init__(self, rest_name, cusine_type):
        self.name = rest_name
        self.type = cusine_type
        self.number_served = 0

    def des_restaurant(self):
        print(self.name + ' is name! and type : '+self.type)

    def open_restaurant(self):
        print('restaurant is open')

    def set_number_served(self,adj_number):
        self.number_served = adj_number

    def increment_number_served(self,inc_number):
        self.number_served += inc_number



my_res = Restaurant('outback','family')

my_res.des_restaurant()
my_res.open_restaurant()
print(my_res.number_served)
my_res.number_served = 10
print(my_res.number_served)
my_res.set_number_served(3)
print(my_res.number_served)
my_res.increment_number_served(5)
print(my_res.number_served)