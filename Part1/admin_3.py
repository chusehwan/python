
import admin_2

class Privileges():
    def __init__(self):
        self.pri = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for p in self.pri:
            print(p + '.')

class Admin(admin_2.User):
    def __init__(self,first_name, last_name):
        super().__init__(first_name,last_name)
        self.pri =Privileges()
