<<<<<<< HEAD
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

#Bad Method
combined = letters + numbers +  names
print(combined)  #['a', 'b', 'c', 'd', 0, 1, 2, 3, 'Corey', 'Nicole']


combined = itertools.chain(letters, numbers,  names)
print(combined)  #<itertools.chain object at 0x0000017CFFEB8AF0>

for item in combined:
    print(item)

'''
a
b
c
d
0
1
2
3
Corey
Nicole
=======
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

#Bad Method
combined = letters + numbers +  names
print(combined)  #['a', 'b', 'c', 'd', 0, 1, 2, 3, 'Corey', 'Nicole']


combined = itertools.chain(letters, numbers,  names)
print(combined)  #<itertools.chain object at 0x0000017CFFEB8AF0>

for item in combined:
    print(item)

'''
a
b
c
d
0
1
2
3
Corey
Nicole
>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
'''