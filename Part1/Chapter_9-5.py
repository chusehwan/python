#Login Attempts

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        name = self.first_name + self.last_name
        print('full name is : ' + name)

    def greet_user(self):
        name = self.first_name + self.last_name
        print('Welcome! : ' + name)

    def increment_login_attempts(self):
        self.login_attempts+=2

    def reset_login_attempts(self):
        self.login_attempts = 0

abc = User('chu', 'sehwan')

print(abc.login_attempts)
a = 0
while a<10:
    abc.increment_login_attempts()
    print(abc.login_attempts)
    a+=1

abc.reset_login_attempts()
print(abc.login_attempts)
