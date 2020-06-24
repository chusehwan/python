#Employee

class Employee():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = 0

    def give_raise(self,add_amount=0):
        if add_amount != 0:
            self.annual_salary += add_amount
        else:
            self.annual_salary +=5000
        return self.annual_salary
