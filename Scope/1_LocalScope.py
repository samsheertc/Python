'''
LEGB
Local, Enclosing, Global, Built-in
'''

#eg-1
#[checked y in local section and found]
x = 'global x'
def test():
    y = 'local y'
    print(y) #local y
test()


#eg-2
#[checked x in local section and not found]
#[checked x in enclosing section and not found]
#[checked x in global section and found]
x = 'global x'
def test():
    y = 'local y'
    print(x) #global x
test()


#eg-3				   
#Error
#[y has no scope outside of test function]
#[no y variable in Local, Enclosing, Global or Built-in]
x = 'global x'
def test():
    y = 'local y'
    print(x)
test()
print(y)


#eg-4
x = 'global x'
def test():
    y = 'local y'
    print(x) #global x
test()
print(x) #global x


#eg-5
x = 'global x'
def test():
    x = 'local x'
    print(x) #local x
test()
print(x) #global x


#eg-6
x = 'global x' #we can add this or remove. Doesnt matter
def test():
    global x
    x = 'local x'
    print(x) #local x
test()
print(x) #local x


#eg-7
#Error
#Removed global variable
def test():
    x = 'local x'
    print(x)
test()
print(x)

#eg-8
def test(z):
    x = 'local x'
    print(z)    #local z
test('local z')


#eg-9
#Error as z is not found outside the function
def test(z):
    x = 'local x'
    print(z)
test('local z')
print(z)
