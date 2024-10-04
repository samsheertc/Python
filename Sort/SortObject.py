#List
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)                  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
s_li = sorted(li, reverse=True)    #[9, 8, 7, 6, 5, 4, 3, 2, 1]
print('Sorted Variable:\t', s_li)
li.sort()                          #[1, 2, 3, 4, 5, 6, 7, 8, 9]
li.sort(reverse=True)              #[9, 8, 7, 6, 5, 4, 3, 2, 1]
print('Original Variable:\t', li)


#tuple
tup=(9,1,8,2,7,3,6,4,5)
#tup.sort() #error
print('Tuple\t',tup)    #Tuple	 (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple\t',s_tup)  #Tuple	 [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Dictionary
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t',s_di)    #Dict	 ['age', 'job', 'name', 'os']



#Key Sort
li = [-6, -5, -4, 1, 2, 3]
print(li)          #[-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(s_li)        #[-6, -5, -4, 1, 2, 3]


li = [-6, -5, -4, 1, 2, 3]
print(li)                  #[-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)                #[1, 2, 3, -4, -5, -6]
