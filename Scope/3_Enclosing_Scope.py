#Enclosing Example

#eg-1
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x) #inner x [looks for x in local scope and it is found]
    inner()
    print(x)     #outer x [looks for x local scope and it is found]
outer()

#eg-2
def outer():
    x = 'outer x'
    def inner():
        print(x) #outer x [Looks for x in local scope but not found. But x is there in local scope of Enclosing function]
    inner()
    print(x)     #outer x [Looks for x local scope and it is found]
outer()

#eg-3
#Error
def outer():
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
outer()

#eg-4
#Change the outer function variable
def outer():
    x = 'outer x'
    def inner():
        nonlocal x    #inner x [This will allow us work on local variables of enclosing function]
        x = 'inner x' #inner x [This will affect the x variable of outer function]
        print(x)
    inner()
    print(x)
outer()

#eg-5
#Wrap-up
x = 'global x'
def outer():
    #x = 'outer x'      #try with and without this command
    def inner():
        #x = 'inner x'  #try with and without this command
        print(x)
    inner()
    print(x)
outer()
print(x)
