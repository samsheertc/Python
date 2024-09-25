#min, max, sum
cources = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]
print(min(nums)) #1
print(max(nums)) #5
print(sum(nums)) #15
print(min(cources)) #CompSci
print(max(cources)) #Physics

#Checking an item
cources = ['History', 'Math', 'Physics', 'CompSci']
print(cources.index('CompSci')) #3
print('Art' in cources)         #False
print('Math' in cources)        #True


#Looping a list
cources = ['History', 'Math', 'Physics', 'CompSci']
for item in cources:
    print(item)
  
for idx,cource in enumerate(cources,start=1):
    print(idx,cource)


#List to String
cources = ['History', 'Math', 'Physics', 'CompSci']
cources_str = '-'.join(cources)
print(cources_str)  #History-Math-Physics-CompSci

#String to List
new_list = cources_str.split('-')
print(new_list)   #['History', 'Math', 'Physics', 'CompSci']
