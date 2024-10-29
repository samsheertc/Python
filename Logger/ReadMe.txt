print(logging.DEBUG)     #10
print(logging.INFO)      #20
print(logging.WARNING)   #30
print(logging.WARN)      #30
print(logging.ERROR)     #40
print(logging.CRITICAL)  #50
print(logging.FATAL)     #50

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

logging.debug('This is a debug message')        #2024-10-29 14:06:39,854:root:DEBUG:This is a debug message
logging.info('This is a info message')          #2024-10-29 14:06:39,854:root:INFO:This is a info message
logging.warning('This is a warning message')    #2024-10-29 14:06:39,854:root:WARNING:This is a warning message
logging.error('This is an error message')       #2024-10-29 14:06:39,854:root:ERROR:This is an error message
logging.critical('This is a critical message')  #2024-10-29 14:06:39,854:root:CRITICAL:This is a critical message
logging.fatal('This is a fatal message')        #2024-10-29 14:06:39,855:root:CRITICAL:This is a fatal message

------------------------------------------------------------------------------------------------------------------------
logging.getLogger()
logging.getLogger().setLevel()
logging.getLogger().addHandler()

logging.basicConfig()

logging.Formatter()
logging.Formatter().format
logging.Formatter().datefmt
logging.Formatter().formatMessage

logging.FileHandler()
logging.FileHandler('sample.log').setLevel()
logging.FileHandler('sample.log').setFormatter()

logging.StreamHandler()
logging.StreamHandler().setFormatter
logging.StreamHandler().setLevel
logging.StreamHandler().set_name
logging.StreamHandler().setStream
logging.StreamHandler().formatter


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
------------------------------------------------------------------------------------------------------------------------

    

      
