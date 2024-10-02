
# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'CompSci'}
print('Math' in cs_courses) #True


#Operation On Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses)) #{'Math', 'History'}
print(cs_courses.difference(art_courses))   #{'CompSci', 'Physics'}
print(cs_courses.union(art_courses))        #{'History', 'Art', 'Design', 'Math', 'Physics', 'CompSci'}



# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}     # This isn't right! It's a dict
empty_set = set()
