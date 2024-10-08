''' JavaScript Object Notation '''

'''
conversion logic of string to python object
JSON             PYTHON
{object}      -> dictionary
[array]       -> list
string        -> str
number(int)   -> int
number(real)  ->float
true          ->True
false         ->False
null          -> None

Below String almost Looks like a Python Dictionary
Key = people
Value = Array of objects
Each object is a dictionary with a Key of name, phone, email and has_license
'''

import json
people_string = '''
{
	"people": [
		{
			"name": "John Smith",
			"phone": "615-555-7164",
			"emails": [
				"johnsmith@bogusemail.com",
				"john.smith@work-place.com"
			],
			"has_license": "false"
		},
		{
			"name": "Jane Doe",
			"phone": "560-555-5153",
			"emails": null,
			"has_license": "true"
		}
	]
}
'''

#Convert the above JSON String to Python Object
data = json.loads(people_string)
print(data)
print(type(data))           #<class 'dict'>
print(type(data['people'])) #<class 'list'>

for person in data['people']:
    print(type(person))    #<class 'dict'>
    print(person['name'])

#Convert Python Object to JSON
#Delete the phone tag and create a new JSON
for person in data['people']:
    del person['phone']

print(data) #Phone Number is got deleted

#Dump the converted string to JSON
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
