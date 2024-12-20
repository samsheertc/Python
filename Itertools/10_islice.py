<<<<<<< HEAD
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']


result = itertools.islice(range(10),5)       #5 is stopping value
print(list(result))  #[0, 1, 2, 3, 4]


result = itertools.islice(range(10),1, 5)    #1 is starting and 5 is stopping value
print(list(result)) #[1, 2, 3, 4]



result = itertools.islice(range(10),1, 5, 2) #2 is step here
print(list(result)) #[1, 3]


for item in result:
    print(item)

	
#Practical Scenario
import itertools

with open('test.log', 'r') as f:
    header = itertools.islice(f, 3) #Grab first three lines
    for line in header:
        print(line, end='')

'''
Date: 2018-11-08
Author: Corey
Description: This is a sample log file
'''


##Files are iterators
with open('test.log', 'r') as f:
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')

'''
Date: 2018-11-08
Author: Corey
Description: This is a sample log file
=======
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']


result = itertools.islice(range(10),5)       #5 is stopping value
print(list(result))  #[0, 1, 2, 3, 4]


result = itertools.islice(range(10),1, 5)    #1 is starting and 5 is stopping value
print(list(result)) #[1, 2, 3, 4]



result = itertools.islice(range(10),1, 5, 2) #2 is step here
print(list(result)) #[1, 3]


for item in result:
    print(item)

	
#Practical Scenario
import itertools

with open('test.log', 'r') as f:
    header = itertools.islice(f, 3) #Grab first three lines
    for line in header:
        print(line, end='')

'''
Date: 2018-11-08
Author: Corey
Description: This is a sample log file
'''


##Files are iterators
with open('test.log', 'r') as f:
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')

'''
Date: 2018-11-08
Author: Corey
Description: This is a sample log file
>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
'''