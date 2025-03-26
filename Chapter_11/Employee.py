class Employee:
    def __init__(self,fname,lname,annual_salary):
        self.first_name = fname
        self.last_name = lname
        self.annual_salary = annual_salary
    
    def give_raise(self,pay_raise=5000):
        self.annual_salary = self.annual_salary + pay_raise