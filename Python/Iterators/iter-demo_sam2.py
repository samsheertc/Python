#Practical Usage
#We can add the iterators to classses and we can make them Iterable also

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

#Class for Iterator
nums = MyRange(1, 10)
for num in nums:
    print(num)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

#Generator
nums = my_range(1,10)
for num in nums:
	print(num)

print(next(nums))
print(next(nums))
print(next(nums))

Generators are iterators as well but the dunder __iter__ and dunder __next__ methods are created automatically

Iterators can go for ever

As long as there is a next function it will go for ever 



Iterators can go for ever but it still only fetches one value at a time
This really comes very handy when writing memotry efficient programs
some times there are so many values that you just couldnt hold them all in memory if you were to put them in a list or tuple 
but if you simply use an iterator then you can loop over one value at a time until its exhausted or just let it keep going 
#Generator for Infinite Number Generation
def my_range(start):
    current = start
    while True:
        yield current
        current += 1

nums = my_range(1)
for num in nums:
    print(num)
	
	
Iterator can go on forever but it still only fetches one value at a time 

now this really comes in handy when writing memory efficient programs because sometimes there are so many values that you just couldn't hold

them all in memory if you were to put them in a list or a tuple 

but if you simply use an iterator then you can loop over one value at a time until it's exhausted or just let it keep going so

for example let's say that you were writing a password cracker and wanted to brute-force it by checking all of the

possible password using a certain group of characters 

Well there would be so many different possible passwords that you couldn't possibly hold them all in a single list

your computer would just run out of memory but you could use an iterator to loop through all those possibilities one

at a time and it might take some time until you find a result but your program wouldn't take up all of your computer's

memory and it wouldn't crash 

