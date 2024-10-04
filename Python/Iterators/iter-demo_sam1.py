'''
Iterable is something that can be looped over.

For example a List is iterable because we can loop over a list

List is Iterable but not an iterator.

If we run the dunder method on List it will become an iterator
'''

nums = [1, 2, 3]
for num in nums:
	print(num)


If something is Iterable it needs to have a special method called a dunder method called __iter__()

Iterator is an object with a state so that it remembers where it is during iteration.

#Check the method avaiable for a List
nums = [1, 2, 3]
print(dir(nums))  #__iter__
print(next(nums)) #Error

#Convert List to an Iterator
i_nums = nums.__iter__()
i_nums = iter(nums)

print(i_nums)       #<list_iterator object at 0x000002B0A33E2BF0>
print(dir(i_nums))  #__next__ and __iter__
print(next(i_nums))
print(next(i_nums))




nums = [1, 2, 3]
i_nums = iter(nums)
while True:
	try:
		item = next(i_nums)
		print(item)
	except StopIteration:
		break
