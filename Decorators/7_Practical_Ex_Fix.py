from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

import time
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)

#display_info.log
#INFO:root:Ran with args: ('John', 25), and kwargs: {}

#display_info ran with arguments (John, 25)
#display_info ran in: 2.014810800552368 sec



import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments ({}, {})'.format(name, age))
display_info('John', 25)

#display_info.log
#INFO:root:Ran with args: ('John', 25), and kwargs: {}

#display_info ran with arguments (John, 25)
#display_info ran in: 2.00071382522583 sec
#------------------------------------------------------------------------------------
display_info = my_timer(display_info)
print(display_info.__name__)
display_info('John', 25)

#o/p
#display_info
#display_info ran with arguments (John, 25)
#display_info ran in: 2.0089986324310303 sec

#------------------------------------------------------------------------------------
display_info = my_logger(display_info)
print(display_info.__name__)
display_info('John', 25)

#o/p
#display_info
#display_info ran with arguments (John, 25)
#------------------------------------------------------------------------------------