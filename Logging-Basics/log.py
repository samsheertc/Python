import logging

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.warning('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.warning('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))

logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))   #This wont be printed as default is WARNING
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))   #This wont be printed as default is WARNING
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))   #This wont be printed as default is WARNING
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))   #This wont be printed as default is WARNING


