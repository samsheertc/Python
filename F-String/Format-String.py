first_name = 'Corey'
last_name = 'Schafer'
sentence = 'My Name is {} {}'.format(first_name, last_name)
print(sentence)

sentence = f'My Name is {first_name} {last_name}'
sentence = f'My Name is {first_name.upper()} {last_name.upper()}'
print(sentence)

person = {'name': 'Jenn', 'age': 23}
sentence = 'My Name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)

sentence2 = f"My Name is {person['name']} and I am {person['age']} years old"
sentence1 = f'My Name is {person['name']} and I am {person['age']} years old'
print(sentence1)
print(sentence2)

calculation = f'4 times 11 is equal to {4 * 11}'
print(calculation)

for n in range(1,11):
    sentence = f'The value is {n:02}'
    print(sentence)

pi = 22/7
sentence = f'Pi is equal to {pi:.4f}'
print(sentence)

import datetime
birthday = datetime.datetime(1984, 10, 31)
sentence = f'Samsheer has a birthday on {birthday:%B %d, %Y}'
print(sentence)
