import itertools
import operator

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

result = itertools.accumulate(numbers)
print(list(result)) #[0, 1, 3, 6, 8, 9, 9]

for item in result:
    print(item)




numbers = [0, 1, 2, 3, 2, 1, 0]  
result = itertools.accumulate(numbers, operator.mul)
print(list(result))
#[0, 0, 0, 0, 0, 0, 0]


numbers = [1, 2, 3, 2, 1, 0]
result = itertools.accumulate(numbers, operator.mul)
print(list(result))
#[1, 2, 6, 12, 12, 0]

