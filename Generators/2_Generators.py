#Generator
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)       #<generator object square_numbers at 0x000002E2BFED2650>
print(next(my_nums)) #1
print(next(my_nums)) #4
print(next(my_nums)) #9
print(next(my_nums)) #16
print(next(my_nums)) #25

my_nums = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:
    print(num)
