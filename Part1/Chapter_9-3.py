class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        name = self.first_name + self.last_name
        print('full name is : ' + name)

    def greet_user(self):
        name = self.first_name + self.last_name
        print('Welcome! : ' + name)

abc = User('chu', 'sehwan')

abc.describe_user()
abc.greet_user()