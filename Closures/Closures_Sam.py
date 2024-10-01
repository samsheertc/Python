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

#eg-1
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()    #this contains the inner function to be executed 
print(my_func)            #<function outer_func.<locals>.inner_func at 0x000001F6062E70A0>
print(my_func.__name__)   #inner_func
my_func()                 #Hi
my_func()                 #Hi
my_func()                 #Hi


#eg-2
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')       #this contains the inner function to be executed 
hello_func = outer_func('Hello') #this contains the inner function to be executed 

hi_func()                #Hi
hello_func()             #Hello



#eg-3
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)
def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3, 3)
add_logger(4, 5)
sub_logger(10, 5)
sub_logger(20, 10)
