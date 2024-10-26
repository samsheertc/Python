import itertools

def lt_2(n):
    if n < 2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']



result = itertools.takewhile(lt_2, numbers)
for item in result:
    print(item)

'''
0
1
'''