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
