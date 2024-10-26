<<<<<<< HEAD
import itertools

def lt_2(n):
    if n < 2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]


result = itertools.dropwhile(lt_2, numbers)
for item in result:
    print(item)

'''
2
3
2
1
0
'''



'''
stop filtering once a function returns true
dropwhile function will drop values from an iterable until one of the values returns True
=======
import itertools

def lt_2(n):
    if n < 2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]


result = itertools.dropwhile(lt_2, numbers)
for item in result:
    print(item)

'''
2
3
2
1
0
'''



'''
stop filtering once a function returns true
dropwhile function will drop values from an iterable until one of the values returns True
>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
'''