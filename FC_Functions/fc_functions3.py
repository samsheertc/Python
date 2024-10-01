# Here the logger function returns function "log_message "

def logger(msg):
    def log_message():
        print('Log:',msg)
    return log_message

log_hi = logger('Hi!')
log_hi()    #Log: Hi!
