#Load JSON files to Python Object
import json

with open('states.json') as f:
	data = json.load(f)

#This also works instead of with open
data = json.load(open('states.json'))
print(data)


print(type(data))                            #<class 'dict'>
print(type(data['states']))                  #<class 'list'>
print(type(data['states'][0]))               #<class 'dict'>
print(type(data['states'][0]['area_codes'])) #<class 'list'>

for state in data['states']:
	print(state)
	print(state['name'])
	print(state['abbreviation'])
	print(state['area_codes'])
	print()




#Modify Python objects and load back to JSON file
import json
with open('states.json') as f:
	data = json.load(f)

for state in data['states']:
	del state['area_codes']

print(data)

with open('new_states.json', 'w') as f:
	json.dump(data, f, indent=2)




