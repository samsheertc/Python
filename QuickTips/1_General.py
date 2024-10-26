#-------------------------------------------------
#Normal if 
condition = False
if condition:
    x = 1
else:
    x = 0
print(x)

#Ternary Conditionals 
condition = True
x = 1 if condition else 0
print(x)

#-------------------------------------------------
#Underscore Placeholders
num1 = 10000000000
num2 = 100000000
total = num1 + num2
print(total)

num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')

#-------------------------------------------------
#Context Managers
f = open('test.txt', 'r')
file_contents = f.read()
f.close()

with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
#-------------------------------------------------
#Enumerate
names = ['Corey', 'Chris', 'Dave', 'Travis']
index = 0
for name in names:
    print(index, name)
    index += 1

for index, name in enumerate(names, start=1):
    print(index, name)
#-------------------------------------------------
#Zip
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes =  ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heroes, universes):
    print(value)
#-------------------------------------------------
