#eg-1
#sort method
cources = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

cources.sort()
nums.sort()

print(cources) #['CompSci', 'History', 'Math', 'Physics']
print(nums)    #[1, 2, 3, 4, 5]




#eg-2
cources = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

cources.sort(reverse=True)
nums.sort(reverse=True)

print(cources) #['Physics', 'Math', 'History', 'CompSci']
print(nums)    #[5, 4, 3, 2, 1]




#eg-3
#sorted function
cources = ['History', 'Math', 'Physics', 'CompSci']

sorted_cources = sorted(cources)

print(cources)         #['History', 'Math', 'Physics', 'CompSci']
print(sorted_cources)  #['CompSci', 'History', 'Math', 'Physics']





#eg-4
#sorted function
cources = ['History', 'Math', 'Physics', 'CompSci']

sorted_cources = sorted(cources, reverse=True)

print(cources)         #['History', 'Math', 'Physics', 'CompSci']
print(sorted_cources)  #['Physics', 'Math', 'History', 'CompSci']
