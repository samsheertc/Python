#Python OOP Tutorial 5: Special (Magic/Dunder) Methods
#https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6

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

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1)       #[Employee('Corey','Schafer',50000)]        calls __repr__ method if no __str__ is defined   
                   #[Corey Schafer - Corey.Schafer@email.com]  calls __str__ method if  __str__ is defined   

print(str(emp_1))  #[Employee('Corey','Schafer',50000)]        calls __repr__ method if no __str__ is defined   
                   #[Corey Schafer - Corey.Schafer@email.com]  calls __str__ method if  __str__ is defined

#Employee('Corey','Schafer',50000)
print(repr(emp_1)) 
print(emp_1.__repr__())

#Corey Schafer - Corey.Schafer@email.com
print(str(emp_1))
print(emp_1.__str__())

print("-----------------------------")
print(1+2)                     #3
print(int.__add__(1,2))        #3
print('a'+'b')                 #ab
print(str.__add__('a','b'))    #ab
print(emp_1 + emp_2)           #110000

print("-----------------------------")
print(len('samsheer'))         #8
print(str.__len__('samsheer')) #8
print('samsheer'.__len__())    #8

print("-----------------------------")
print(len(emp_1))               #13
#print(str.__len__(emp_1))      #Error
print(emp_1.__len__())          #13
print("-----------------------------")
