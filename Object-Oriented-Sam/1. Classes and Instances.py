#Python OOP Tutorial 1: Classes and Instances
#https://www.youtube.com/watch?v=ZDa-Z5JzLYM

#------------------------------------------------------------------
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

#------------------------------------------------------------------
#Class Attributes ->first, last, pay ,email
#Class Method     ->fullname()
#__init__         ->Constructor

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', '60000')

print(emp_1)                        #<__main__.Employee object at 0x000001B8084A3A00>
print(emp_2)                        #<__main__.Employee object at 0x000001B8084A1390>
						            
print(emp_1.email)                  #Corey.Schafer@company.com
print(emp_2.email)                  #Test.User@company.com
						            
print(emp_1.fullname())             #Corey Schafer
print(emp_2.fullname())             #Test User

print(emp_1.fullname())             #Corey Schafer
print(Employee.fullname(emp_1))     #Corey Schafer
#------------------------------------------------------------------