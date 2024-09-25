def hello_func():
    #pass
    #print('Hello')   #Can Print w/o return
    return 'Hello'
print(hello_func)  #Print memory
print(hello_func())
hello_func()

def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi','Sam'))
print(hello_func('Hi',name='Corey Schafer'))

def student_info(*args , **kwargs):
    print(args)
    print(kwargs)
student_info('Math','Art', name='John',age=22)

def student_info(*args , **kwargs):
    print(args)
    print(kwargs)
cources = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(cources, info)

def student_info(*args , **kwargs):
    print(args)
    print(kwargs)
cources = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(cources, info)
student_info(*cources, **info)
