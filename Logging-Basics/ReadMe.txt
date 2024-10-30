#---------------------------------------------------------------------------------------------------------------------------------
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

Default level for logging is set to WARNING. It will capture everything that is a WARNING or above
So by default it will log WARNING, ERROR and CRITICAL. It will ignore INFO and DEBUG log statements
#---------------------------------------------------------------------------------------------------------------------------------


#Level values in numbers
logging.DEBUG    = 10
logging.INFO     = 20
logging.WARNING  = 30
logging.ERROR    = 40
logging.CRITICAL = 50


Add log record attributes
https://docs.python.org/3/library/logging.html#logrecord-attributes
