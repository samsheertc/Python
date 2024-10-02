cources = ['History', 'Math', 'Physics', 'CompSci']
print(cources)      #['History', 'Math', 'Physics', 'CompSci']
print(len(cources)) #4
print(cources[3])   #CompSci
print(cources[-1])  #CompSci
print(cources[0:2]) #['History', 'Math']
print(cources[:2])  #['History', 'Math']
print(cources[2:])  #['Physics', 'CompSci']

#Append Method
cources = ['History', 'Math', 'Physics', 'CompSci']
cources.append('Art')
print(cources)   #['History', 'Math', 'Physics', 'CompSci', 'Art']

#insert
cources = ['History', 'Math', 'Physics', 'CompSci']
cources.insert(0,'Art')
print(cources) #['Art', 'History', 'Math', 'Physics', 'CompSci']

cources = ['History', 'Math', 'Physics', 'CompSci']
cources2 = ['Art', 'Education']
cources.insert(0,cources2)
print(cources)    #[['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci']
print(cources[0]) #['Art', 'Education']


#extend
cources = ['History', 'Math', 'Physics', 'CompSci']
cources2 = ['Art', 'Education']
cources.extend(cources2)
print(cources)  #['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']

#remove
cources = ['History', 'Math', 'Physics', 'CompSci']
cources.remove('Math')
print(cources)   #['History', 'Physics', 'CompSci']

popped = cources.pop()
print(popped)  #CompSci
print(cources) #['History', 'Math', 'Physics']

#reverse
cources = ['History', 'Math', 'Physics', 'CompSci']
cources.reverse()
print(cources) #['CompSci', 'Physics', 'Math', 'History']
