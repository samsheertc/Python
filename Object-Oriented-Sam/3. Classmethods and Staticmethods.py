#Python OOP Tutorial 3: classmethods and staticmethods
#https://www.youtube.com/watch?v=rq8cL2XMM5M&t=314s

'''
Regular Method accept instance as first parameter by default. By Convention the argument is self
Class Method accept class as the first parameter by default. By Convention the argument is cls
@classmethod decorator is used to convert regular method to class method
@staticmethod decorator is used to add a Static method. This doesnt pass anything automatically
'''

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


# Pulled from global section
print(Employee.raise_amount)  # 1.04
print(emp_1.raise_amount)     # 1.04
print(emp_2.raise_amount)     # 1.04

#Calling Class method from class itself
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)  # 1.05
print(emp_1.raise_amount)     # 1.05
print(emp_2.raise_amount)     # 1.05

#Calling Class method through Instance -Rare Scenario
emp_1.set_raise_amt(1.06)
print(Employee.raise_amount)  # 1.06
print(emp_1.raise_amount)     # 1.06
print(emp_2.raise_amount)     # 1.06

#Parse String and Create Class Instances
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

#Class Method
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)


#Static Method
import datetime
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))
#####################################################
