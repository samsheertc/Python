cources = ['History', 'Math', 'Physics', 'CompSci']
cources.remove('Math')
print(cources)   #['History', 'Physics', 'CompSci']

popped = cources.pop()
print(popped)  #CompSci
print(cources) #['History', 'Math', 'Physics']

cources = ['History', 'Math', 'Physics', 'CompSci']
cources.reverse()
print(cources) #['CompSci', 'Physics', 'Math', 'History']

cources = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]
cources.sort()
nums.sort()
print(cources) #['CompSci', 'History', 'Math', 'Physics']
print(nums)    #[1, 2, 3, 4, 5]

cources = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]
cources.sort(reverse=True)
nums.sort(reverse=True)
print(cources) #['Physics', 'Math', 'History', 'CompSci']
print(nums)    #[5, 4, 3, 2, 1]

cources = ['History', 'Math', 'Physics', 'CompSci']
sorted_cources = sorted(cources)
print(cources)         #['History', 'Math', 'Physics', 'CompSci']
print(sorted_cources)  #['CompSci', 'History', 'Math', 'Physics']

