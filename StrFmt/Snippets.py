lis = ['Samsheer', 39]
person = {'name': 'Jenn', 'age': 23}

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Jack', '33')

#Dictionaries
sentence = "My Name is {} and I am {} old".format(person['name'], person['age'])
sentence = "My Name is {0} and I am {1} old".format(person['name'], person['age'])
sentence = "My Name is {0[name]} and I am {1[age]} old".format(person, person)
sentence = "My Name is {0[name]} and I am {0[age]} old".format(person)

#List
sentence = "My Name is {0[0]} and I am {0[1]} old".format(lis)


#Class Objects
sentence = "My Name is {0} and I am {1} old".format(p1.name, p1.age)
sentence = "My Name is {0.name} and I am {0.age} old".format(p1)

#Key word Argument
sentence = "My Name is {name} and I am {age} old".format(name='Jenn', age='23')

#Unpacked Object
sentence = 'My name is {name} and I am {age} years old.'.format(**person)

#Math Operation
i=1
pi = 22/7
import datetime
sentence = 'The value is {:03}'.format(i)
sentence = 'Pi is equal to {:.4f}'.format(pi)
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)

# Date Value
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
sentence = '{:%B %d, %Y }'.format(my_date)

print(sentence)
