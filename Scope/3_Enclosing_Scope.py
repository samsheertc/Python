#Enclosing Example

def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x) #inner x [looks for x in local section and it is found]
    inner()
    print(x)     #outer x [looks for x local section and it is found]
outer()

def outer():
    x = 'outer x'
    def inner():
        print(x) #outer x [looks for x in local section but not found. But x is there in local scope of Enclosing function]
    inner()
    print(x)     #outer x [looks for x local section and it is found]
outer()


#Error
def outer():
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
outer()

#Change the outer function variable
def outer():
    x = 'outer x'
    def inner():
        nonlocal x    #inner x [this will allow us work on local variables of enclosing function]
        x = 'inner x' #inner x [this will affect the x variable of outer function]
        print(x)
    inner()
    print(x)
outer()

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
