import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']



result = itertools.permutations(letters, 2)

for item in result:
    print(item)

'''
('a', 'b')
('a', 'c')
('a', 'd')
('b', 'a')
('b', 'c')
('b', 'd')
('c', 'a')
('c', 'b')
('c', 'd')
('d', 'a')
('d', 'b')
('d', 'c')
'''

