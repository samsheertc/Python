<<<<<<< HEAD
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
=======
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
>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
