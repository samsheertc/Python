'''
Decorator is a function that takes another function as an argument and 
Adds some kind of functionality and then returns another function 
all of this with out altering the source code of the original function that you passed in
'''

#Sample Decorator accepting a variable as argument
def decorator_function(message):
	def wrapper_function():
		print(message)
	return wrapper_function


#6:33 - 8:10
#Sample Decorator accepting a function as argument
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('Display function ran')

decorated_display = decorator_function(display)
decorated_display()
-------------------------------------------------------------------------------------------------------
#Code-1
# Sample Decorator accepting a function as argument
#8:20
def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('Display function ran')

display = decorator_function(display)
display() #Wrapper executed this before display
          #Display function ran


#9:24 - #11:17
#Code-1 in decorator tag
def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('Display function ran')

display()               #Wrapper executed this before display
                        #Display function ran
						
print(display.__name__) #wrapper_function
-------------------------------------------------------------------------------------------------------
@decorator_function
 def display():
is equivalent to
display = decorator_function(display).
-------------------------------------------------------------------------------------------------------
