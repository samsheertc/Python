#Python OOP Tutorial 2: Class Variables
#https://www.youtube.com/watch?v=BJ-VvGyQxho

class Employee:
    num_of_emps = 0     #Class Variable1
    raise_amount = 1.04 #Class Variable2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int( self.pay * self.raise_amount ) #we can use self.raise_amount or Employee.raise_amount based on the need 

print(Employee.num_of_emps)   #0
emp_1 = Employee('Corey', 'Schafer', 50000)
print(Employee.num_of_emps)   #1
emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_emps)   #2

print(emp_1.pay)             #50000
emp_1.apply_raise()          
print(emp_1.pay)             #50000*1.04=52000

print(Employee.raise_amount) #1.04
print(emp_1.raise_amount)    #1.04 [It first check if the Instance has any attribute with name "raise_amount". If it not found then check the class or Inherited class has this attribute "raise_amount"]
print(emp_2.raise_amount)    #1.04 [same as above]


print(Employee.__dict__)     #{'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x000002041D3D05E0>, 'fullname': <function Employee.fullname at 0x000002041D3D0670>, 'apply_raise': <function Employee.apply_raise at 0x000002041D3D0700>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
print(emp_1.__dict__)        #{'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com'}
print(emp_2.__dict__)        #{'first': 'Test', 'last': 'User', 'pay': '60000', 'email': 'Test.User@company.com'}


Employee.raise_amount = 1.05 #Here raise amount will be shared across all Instances 
print(Employee.raise_amount) #1.05
print(emp_1.raise_amount)    #1.05
print(emp_2.raise_amount)    #1.05
print(Employee.__dict__)     #{'__module__': '__main__', 'num_of_emps': 2, 'raise_amount': 1.05, '__init__': <function Employee.__init__ at 0x0000015C8DF305E0>, 'fullname': <function Employee.fullname at 0x0000015C8DF30670>, 'apply_raise': <function Employee.apply_raise at 0x0000015C8DF30700>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
print(emp_1.__dict__)        #{'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com'}
print(emp_2.__dict__)        #{'first': 'Test', 'last': 'User', 'pay': '60000', 'email': 'Test.User@company.com'}


emp_1.raise_amount = 1.05    #{Here raise_amount=1.05 will be a separate attribute under emp_1 instance]
print(Employee.raise_amount) #1.04
print(emp_1.raise_amount)    #1.05
print(emp_2.raise_amount)    #1.04 [emp_2 still uses Class Variable]
print(Employee.__dict__)     #{'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x0000024753EC05E0>, 'fullname': <function Employee.fullname at 0x0000024753EC0670>, 'apply_raise': <function Employee.apply_raise at 0x0000024753EC0700>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
print(emp_1.__dict__)        #{'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com', 'raise_amount': 1.05}
print(emp_2.__dict__)        #{'first': 'Test', 'last': 'User', 'pay': '60000', 'email': 'Test.User@company.com'}

#Notes
For Class Variable we can use as self.Variable or ClassName.Variable
ClassName.raise_amount make some sense as we can have Common Level of raise_amount across Organization
self.raise_amount make some sense as we can have different level of raise between employees

ClassName.num_of_emps make sense as the total employees under the company
self.num_of_emps doesnt make any sense here
