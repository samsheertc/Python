'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'global x'
def test():
    global x
    x = 'local x'
    y = 'local y'
    print(y) #local y
    print(x) #local x
test()
print(x)
print(y) #Error


import builtins
import sys-
import datetime
print(dir(builtins))
print(dir(sys))
print(dir(datetime))


#Enclosing Example
x = 'global x'
def outer():
    #x = 'outer x'
    def inner():
        #nonlocal x
        #x = 'inner x'
        print(x)
    inner()
    print(x)
outer()
print(x)
