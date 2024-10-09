import builtins
import sys
import datetime
print(dir(builtins))
print(dir(sys))
print(dir(datetime))

import builtins
for func in dir(builtins):
    if func == 'min':
        print(func)

#eg-1
#Here it search for min function in Local, Enclosing and Global Section and not found
#Finally it see the function in Built-In Section
import builtins
m = min([5, 4, 1, 2, 3])
print(m)  #1

#eg-2
#Here it search for min function in Local and then found
#Since the local function doesnt  accept arguments it become error
#TypeError: min() takes 0 positional arguments but 1 was given
import builtins
def min():
    pass
m = min([5, 4, 1, 2, 3])
print(m)

#eg-3
#Looks Built in Sections
import builtins
def my_min():
    pass
m = min([5, 4, 1, 2, 3])
print(m) #1

#eg-4
#Here it search for min function in Local and then found
#Since the local function accepts arguments it prints the first 2 elements of list
import builtins
def min(list):
    return list[:2]
m = min([5, 4, 1, 2, 3])
print(m) #[5, 4]
