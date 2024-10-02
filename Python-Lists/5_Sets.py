
#Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

#Order in each run
#{'Physics', 'Math', 'History', 'CompSci'}
#{'Math', 'Physics', 'History', 'CompSci'}
#{'CompSci', 'Physics', 'Math', 'History'}
#{'Physics', 'Math', 'CompSci', 'History'}
#{'Physics', 'History', 'Math', 'CompSci'}

#Dups are removed
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses) 
#{'CompSci', 'History', 'Physics', 'Math'}


#Membership Test
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'CompSci'}
print('Math' in cs_courses) #True


#Operation On Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses)) #{'Math', 'History'}
print(cs_courses.difference(art_courses))   #{'CompSci', 'Physics'}
print(cs_courses.union(art_courses))        #{'History', 'Art', 'Design', 'Math', 'Physics', 'CompSci'}
