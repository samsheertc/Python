import logging

#To log DEBUG/INFO
logging.basicConfig(level=logging.DEBUG)

#create log file
logging.basicConfig(filename='test.log', level=logging.DEBUG)

#Level values in numbers
#logging.DEBUG    = 10
#logging.INFO     = 20
#logging.WARNING  = 30
#logging.ERROR    = 40
#logging.CRITICAL = 50

#add log record attributes
#https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
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
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
