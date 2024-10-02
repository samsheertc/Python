#Create Generators from Comprehension

my_nums =(x*x for x in [1, 2, 3, 4, 5])
print(my_nums)       #<generator object <genexpr> at 0x0000023858A02570>
print(list(my_nums)) #[1, 4, 9, 16, 25]

for num in my_nums:
    print(num)


#List Comprehension
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)  #[1, 4, 9, 16, 25]
