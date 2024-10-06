#Python OOP Tutorial 4: Inheritance - Creating Subclasses
#https://www.youtube.com/watch?v=RSl87lqOXDE&t=614s

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
	pass
	#raise_amount = 1.10

#Option-1
dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'User', 60000)
print(dev_1.email) #Corey.Schafer@email.com
print(dev_2.email) #Test.User@email.com

#Option-2
dev_1 = Developer('Corey', 'Schafer', 50000)  #Looks for Developer class for init method and if not found look for parent class Employee's init method
dev_2 = Developer('Test', 'User', 60000)
print(dev_1.email) #Corey.Schafer@email.com
print(dev_2.email) #Test.User@email.com


#Do Option-2 and then follow below steps
print(dev_1.pay)     #50000 
dev_1.apply_raise()
print(dev_1.pay)     #52000  [when raise_amount = 1.04 defined as Employee class Variable and nothing added under Developer Class]

print(dev_1.pay)     #50000
dev_1.apply_raise()
print(dev_1.pay)     #55000 [when raise_amount = 1.10 under Developer class]



#Do Option-1 then follow below
print(dev_1.pay)     #50000
dev_1.apply_raise()
print(dev_1.pay)     #52000 [when raise_amount = 1.04 as Employee class variable + raise_amount = 1.10 under Developer class]
                     #Changing in Subclass doesnt alter the parent class

'''
help(Developer)
class Developer(Employee)
 |  Developer(first, last, pay)
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object

 |  Methods inherited from Employee:
 |  __init__(self, first, last, pay)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  apply_raise(self)
 |  fullname(self)
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |  raise_amount = 1.04
'''



class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10
	
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay) this also works
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): #employees=[] not recommended .Pass a Mutable Datatype is not recommeneded
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('---->',emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000 ,'Java')
print(dev_1.email)     #Corey.Schafer@email.com
print(dev_1.prog_lang) #Python

mgr_1 = Manager('Sue','Smith',90000, [dev_1])
print(mgr_1.email)     #Sue.Smith@email.com
mgr_1.add_emp(dev_2)

print('After Add')
mgr_1.print_emp()
'''
----> Corey Schafer
----> Test User
'''

print('After delete')
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
'''
After delete
----> Test User
'''

print(isinstance(mgr_1,Manager))   #True
print(isinstance(mgr_1,Employee))  #True
print(isinstance(mgr_1,Developer)) #False

print(issubclass(Developer,Employee)) #True
print(issubclass(Manager,Employee))   #True
print(issubclass(Manager,Developer))  #False



