import itertools

counter = itertools.repeat(2)

print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2



counter = itertools.repeat(2, times=3)

print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #error
print(next(counter)) #error
print(next(counter)) #error


#No Error
for num in itertools.repeat(2, times=3):
	print(num)





#Real life eg:

import itertools

squares = map(pow, range(10), itertools.repeat(2))
squares_new = map(pow, range(10), itertools.repeat(2, times=3))

print(squares)           #<map object at 0x00000231A7ED8EE0>

print(list(squares))     #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(squares_new)) #[0, 1, 4]


#NOTE : repeat is an infinite iterator
