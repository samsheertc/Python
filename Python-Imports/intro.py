#courses = ['History', 'Math', 'Physics', 'CompSci']

import my_module
find_list = ['Math', 'Phy', 'Eng', 'Bio']
find_str = 'Bio'
pos = my_module.find_index(find_str,find_list)
print(pos)

import my_module as tm
find_list = ['Math', 'Phy', 'Eng', 'Bio']
find_str = 'Bio'
pos = tm.find_index(find_str,find_list)
print(pos)

from my_module import find_index, test
find_list = ['Math', 'Phy', 'Eng', 'Bio']
find_str = 'Bio'
pos = find_index(find_str,find_list)
print(pos)
print(test)

from my_module import find_index as find, test
find_list = ['Math', 'Phy', 'Eng', 'Bio']
find_str = 'Bio'
pos = find(find_str,find_list)
print(pos)
print(test)

from my_module import *
find_list = ['Math', 'Phy', 'Eng', 'Bio']
find_str = 'Bio'
pos = find_index(find_str,find_list)
print(pos)
print(test)
