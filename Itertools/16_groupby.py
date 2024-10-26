import itertools

def get_state(person):
    return person['state']
	
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]
-------------------------------------------------------------------------------------
person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key, group)

#NY <itertools._grouper object at 0x0000023DD1129AE0>
#CO <itertools._grouper object at 0x0000023DD112A320>
#WV <itertools._grouper object at 0x0000023DD1129AE0>
#NC <itertools._grouper object at 0x0000023DD112A320>

#group is an iterator
-------------------------------------------------------------------------------------
for key, group in person_group:
    print(key, len(list(group)))

NY 2
CO 2
WV 2
NC 3
-------------------------------------------------------------------------------------
for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()

NY
{'name': 'John Doe', 'city': 'Gotham', 'state': 'NY'}
{'name': 'Jane Doe', 'city': 'Kings Landing', 'state': 'NY'}

CO
{'name': 'Corey Schafer', 'city': 'Boulder', 'state': 'CO'}
{'name': 'Al Einstein', 'city': 'Denver', 'state': 'CO'}

WV
{'name': 'John Henry', 'city': 'Hinton', 'state': 'WV'}
{'name': 'Randy Moss', 'city': 'Rand', 'state': 'WV'}

NC
{'name': 'Nicole K', 'city': 'Asheville', 'state': 'NC'}
{'name': 'Jim Doe', 'city': 'Charlotte', 'state': 'NC'}
{'name': 'Jane Taylor', 'city': 'Faketown', 'state': 'NC'}
-------------------------------------------------------------------------------------

