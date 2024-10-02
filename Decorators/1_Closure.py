'''
First Class Functions Allows us to treat functions like any other object.
We can pass functions as arguments to another function
We can return functions
and we can assign functions to variables

Closures allow us to take advantage of first-class functions
and return an inner function that remembers and has access to variables local to the scope in which they were created
'''

#Closure eg
def outer_function():
    message = 'Hi'        #free variable
    def inner_function():
        print(message)
    return inner_function

myfunc = outer_function()
myfunc() #Hi
myfunc() #Hi
myfunc() #Hi


def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')
hi_func()  #Hi
bye_func() #Bye


def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')
hi_func()  #Hi
bye_func() #Bye
