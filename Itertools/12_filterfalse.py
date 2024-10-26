<<<<<<< HEAD
import itertools

def lt_2(n):
    if n < 2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]



result = filter(lt_2, numbers)
for item in result:
    print(item)

'''
0
1
'''



result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)

'''
2
3
'''

numbers = [0, 1, 2, 3, 2, 1, 0]
result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)

'''
2
3
2
'''
=======
import itertools

def lt_2(n):
    if n < 2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]



result = filter(lt_2, numbers)
for item in result:
    print(item)

'''
0
1
'''



result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)

'''
2
3
'''

numbers = [0, 1, 2, 3, 2, 1, 0]
result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)

'''
2
3
2
'''
>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
