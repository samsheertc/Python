code_snippets
/Logging-Basics

#---------------------------------------------------------------------------------------------------------------------------------

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.



# Default level for logging is set to WARNING. It will capture everything that is a WARNING or above

# So by default it will log WARNING, ERROR and CRITICAL. It will ignore INFO and DEBUG log statements
#---------------------------------------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------------------------------
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

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
#---------------------------------------------------------------------------------------------------------------------------------