import itertools

counter = itertools.cycle([1,2,3])

print(next(counter)) #1
print(next(counter)) #2
print(next(counter)) #3
print(next(counter)) #1
print(next(counter)) #2
print(next(counter)) #3


Switch = itertools.cycle(('ON', 'OFF'))

print(next(Switch)) #ON
print(next(Switch)) #OFF
print(next(Switch)) #ON
print(next(Switch)) #OFF



#NOTE : cycle is an infinite iterator
