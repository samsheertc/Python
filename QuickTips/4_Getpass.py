#Normal Method
username = input('Username: ')
password = input('Password: ')
print('Logging In....')

#GetPass
from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')
print('Logging In....')
