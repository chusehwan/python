class Restaurant():
    def __init__(self, rest_name, cusine_type):
        self.name = rest_name
        self.type = cusine_type

    def des_restaurant(self):
        print(self.name + ' is name! and type : '+self.type)

    def open_restaurant(self):
        print('restaurant is open')

my_res = Restaurant('outback','family')
your_res = Restaurant('순대국','가정식')
i_res = Restaurant('돈까스','기름집')

my_res.des_restaurant()
your_res.des_restaurant()
i_res.des_restaurant()
