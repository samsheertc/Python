#Class Decorator
#13:20 - 16:30

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print('Display function ran')

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display()  # Call method executed this before display
           # Display function ran

display_info('John', 25) # Call method executed this before display_info
                         # display_info ran with arguments (John, 25)

