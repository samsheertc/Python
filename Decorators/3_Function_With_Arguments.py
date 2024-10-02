#Passing a function with arguments
#11:17 - 13:20

#Passing a function with arguments using decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display() #Wrapper executed this before display
          #Display function ran

display_info('John', 25) #Wrapper executed this before display_info
                         #display_info ran with arguments (John, 25)




#The above code with out using decorator tag
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

def display():
    print('Display function ran')

def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display = decorator_function(display)
display()  #Wrapper executed this before display
           #Display function ran

display_info = decorator_function(display_info)
display_info('John', 25)  #Wrapper executed this before display_info
                          #display_info ran with arguments (John, 25)

