#function to square a list
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums) #[1, 4, 9, 16, 25]

#Read a List
for num in my_nums:
    print(num)
	
	

#Generator
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)  #<generator object square_numbers at 0x000002E2BFED2650>
print(next(my_nums)) #1
print(next(my_nums)) #4
print(next(my_nums)) #9
print(next(my_nums)) #16
print(next(my_nums)) #25

my_nums = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:
    print(num)
	
	
#List Comprehension
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)  #[1, 4, 9, 16, 25]

#Generator
my_nums =(x*x for x in [1, 2, 3, 4, 5])

print(my_nums)       #<generator object <genexpr> at 0x0000023858A02570>
print(list(my_nums)) #[1, 4, 9, 16, 25]


for num in my_nums:
    print(num)
