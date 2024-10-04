1.
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)
s_li = sorted(li, reverse=True)
print('Sorted Variable:\t', s_li)
li.sort()
li.sort(reverse=True)
print('Original Variable:\t', li)


2.
tup=(9,1,8,2,7,3,6,4,5)
tup.sort() #error

print('Tuple\t',tup)  #Tuple	 (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple\t',s_tup)  #Tuple	 [1, 2, 3, 4, 5, 6, 7, 8, 9]

3.
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t',s_di) #Dict	 ['age', 'job', 'name', 'os']



4.
li = [-6, -5, -4, 1, 2, 3]
print(li)          #[-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(s_li)        #[-6, -5, -4, 1, 2, 3]


li = [-6, -5, -4, 1, 2, 3]
print(li)                  #[-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)                #[1, 2, 3, -4, -5, -6]








