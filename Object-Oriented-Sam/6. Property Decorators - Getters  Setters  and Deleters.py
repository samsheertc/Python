#Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters
#https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)       #John
print(emp_1.last)        #Smith
print(emp_1.email)       #John.Smith@email.com
print(emp_1.fullname())  #John Smith

emp_1.first = 'Jim'    ##Let Say First name has changed to Jim

print(emp_1.first)      #Jim
print(emp_1.last)       #Smith
print(emp_1.email)      #John.Smith@email.com  [Email IS NOT changed ]
print(emp_1.fullname()) #Jim Smith             [Full name has changed ]
####################################################################################################################################################

'''
So let say if we need to change the email automatically similar to FullName 
then we need to define a method for email like fullname()
Below Code has added a method email()
But the code which uses email attribute has to be changed to email() method as shown below
'''

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        #return self.first + '.' + self.last + '@email.com'
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)       #John
print(emp_1.last)        #Smith
print(emp_1.email())     #John.Smith@email.com
print(emp_1.fullname())  #John Smith

emp_1.first = 'Jim'      ##Let Say First name has changed to Jim

print("----------------")
print(emp_1.first)       #Jim
print(emp_1.last)        #Smith
print(emp_1.email())     #Jim.Smith@email.com ....Need this to covert as a method in all part of the code
print(emp_1.fullname())  #Jim Smith
####################################################################################################################################################
'''
To Avoid changing the Email attribute to Email method we can introduce Class Decorator like below

'''

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        #return self.first + '.' + self.last + '@email.com'
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)         #John
print(emp_1.last)          #Smith
print(emp_1.email)         #John.Smith@email.com .[No need to access as method using '()' ]
print(emp_1.fullname)      #John Smith            [No need to access as method using '()' ]

emp_1.first = 'Jim'        ##Let Say First name has changed to Jim

print("----------------")
print(emp_1.first)         #Jim
print(emp_1.last)          #Smith
print(emp_1.email)         #Jim.Smith@email.com    [No need to access as method using '()' ]
print(emp_1.fullname)      #Jim Smith              [No need to access as method using '()' ]


####################################################################################################################################################
'''
In the above example if we change the value of propery method we will get ERROR
Let say we are changing the fullname. 
This will cause an error and to fix that see the code below
emp_1.fullname = 'Corey Schafer' ************AttributeError: can't set attribute 'fullname' *********
'''

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        #return self.first + '.' + self.last + '@email.com'
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

	#This is the additional code I have added.
	#If this is added fullname will be read from here. Else it will go to previous one
    @fullname.getter
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
		
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


	
emp_1 = Employee('John', 'Smith')

print(emp_1.first)         #John
print(emp_1.last)          #Smith
print(emp_1.email)         #John.Smith@email.com
print(emp_1.fullname)      #John Smith

emp_1.fullname = 'Corey Schafer' #Lets Change the full name

print("----------------")
print(emp_1.first)         #Corey
print(emp_1.last)          #Schafer
print(emp_1.email)         #Corey.Schafer@email.com
print(emp_1.fullname)      #Corey Schafer

del emp_1.fullname

print("----------------")
print(emp_1.first)         #None
print(emp_1.last)          #None
print(emp_1.email)         #None.None@email.com
print(emp_1.fullname)      #None None
