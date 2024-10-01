'''
A closure is a record storing a function together with an environment:
a mapping associating each free variable of the function
with the value or storage location to which the name was bound when the
closure was created . A closure ,unlilke a plain function , allows the
function to access those captured variables through the closure's
reference to them, even when the function is invoked outside their scope

A closure in an inner function that remembers and has access to variables in the local scope in which
it was created even after the outer function has finished executing

'''

#-------------------------------------------------------------------------------------
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()
print(my_func)            #<function outer_func.<locals>.inner_func at 0x000001F6062E70A0>
print(my_func.__name__)   #inner_func
my_func()                 #Hi
my_func()                 #Hi
my_func()                 #Hi


#-------------------------------------------------------------------------------------
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()    #Hi
hello_func() #Hello
#-------------------------------------------------------------------------------------
