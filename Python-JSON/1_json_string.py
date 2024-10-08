''' JavaScript Object Notation '''
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
    print(type(person))
    print(person['name'])


#Convert Python Object to JSON
#Delete the phone tag and create a new JSON
for person in data['people']:
    del person['phone']

#Phone Number is got deleted
print(data)

#Dumpp the converted string to JSON
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

'''
conversion logic of string to json
{object}      -> dictionary
[array]       -> list
string        -> str
number(int)   -> int
number(real)  ->float
true          ->True
false         ->False
null          -> None
'''
