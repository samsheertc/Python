

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1) #['History', 'Math', 'Physics', 'CompSci']
print(list_2) #['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Art'

print(list_1) #['Art', 'Math', 'Physics', 'CompSci']
print(list_2) #['Art', 'Math', 'Physics', 'CompSci']



# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1) #('History', 'Math', 'Physics', 'CompSci')
print(tuple_2) #('History', 'Math', 'Physics', 'CompSci')

tuple_1[0] = 'Art' #TypeError: 'tuple' object does not support item assignment

print(tuple_1) #('History', 'Math', 'Physics', 'CompSci')
print(tuple_2) #('History', 'Math', 'Physics', 'CompSci')
