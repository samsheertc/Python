#22:00 - onwards

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

import time

#Case-1
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)

#display_info.log
#-----------------
#INFO:root:Ran with args: ('John', 25), and kwargs: {}

#display_info ran with arguments (John, 25)
#wrapper ran in: 2.0149331092834473 sec




#Case-2
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)

#wrapper.log
#-----------
#INFO:root:Ran with args: ('John', 25), and kwargs: {}

#display_info ran with arguments (John, 25)
#display_info ran in: 2.015312433242798 sec

-------------------------------------------------------------------------------------------------
#Try-1
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments ({}, {})'.format(name, age))
	
display_info = my_timer(display_info)
print(display_info.__name__)                     #"wrapper" function is returned
display_info = my_logger(my_timer(display_info)) #wrapper is passed as the argument to logger and hence it created the wrapper.log file


display_info = my_logger(display_info)           #display_info function passed to my_logger and "display_info.log" has created
print(display_info.__name__)                     #wrapper
display_info = my_timer(my_logger(display_info)) #"wrapper" function passed to my_timer and printed accordingly
