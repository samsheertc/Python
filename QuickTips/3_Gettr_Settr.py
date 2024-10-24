################################################################
class Person():
    pass

person = Person()

person.first = 'Corey'
person.last = 'Schafer'

print(person.first)
print(person.last)
################################################################
class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

#person.first_key = first_val #Error
setattr(person, 'first', 'Corey')
setattr(person, 'last', 'Schafer')

print(person.first)
print(person.last)

################################################################
class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_val )
print(person.first)

first = getattr(person, first_key)
print(first)

################################################################
class Person():
    pass

person = Person()

person_info = { 'first' :'Corey', 'last' : 'Schafer' }

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

for key in person_info.keys():
    print(getattr(person, key))
################################################################
