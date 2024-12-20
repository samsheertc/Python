<<<<<<< HEAD
import itertools

counter = itertools.count()

print(counter)       #count(0)
print(type(counter)) #<class 'itertools.count'>
print(next(counter)) #0
print(next(counter)) #1
print(next(counter)) #2
print(next(counter)) #3

#Infinite Loop
for num in counter:
    print(num)

#Practical Scenario
data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))

print(daily_data)  #[(0, 100), (1, 200), (2, 300), (3, 400)]


counter = itertools.count(start=5, step=-2.5)
print(next(counter)) #5
print(next(counter)) #2.5
print(next(counter)) #0
print(next(counter)) #-2.5


#NOTE : count is an infinite iterator
=======
import itertools

counter = itertools.count()

print(counter)       #count(0)
print(type(counter)) #<class 'itertools.count'>
print(next(counter)) #0
print(next(counter)) #1
print(next(counter)) #2
print(next(counter)) #3

#Infinite Loop
for num in counter:
    print(num)

#Practical Scenario
data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))

print(daily_data)  #[(0, 100), (1, 200), (2, 300), (3, 400)]


counter = itertools.count(start=5, step=-2.5)
print(next(counter)) #5
print(next(counter)) #2.5
print(next(counter)) #0
print(next(counter)) #-2.5


#NOTE : count is an infinite iterator
>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
