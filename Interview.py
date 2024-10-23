#1 Know how to write code on a whiteboard or paper

###############################################
#2 Know Basic Python Control Flow
for i in range(1,11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

a = 10
b = 20

if a < b :
    print("{} is less than {}".format(a, b))
elif a == 20:
    print("{} is equal to {}".format(a, b))
else:
    print("{} is greater than {}".format(a, b))
	
###############################################
#3 Be Able to discuss how you have used python

import os, glob
os.chdir("C:/Users/samsh/Google Drive/DR-Videos/Image")
for file in glob.glob("*.jpg"):
    print(file)



###############################################
#4 Know how to solve common interview problems
#Fizz Buzz
for num in range(1,100):
    if num % 5 == 0 and num % 3 ==0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


#Fibonacci Series
a, b = 0, 1
for i in range(0,10):
    print(a)
    a, b = b, a+b

#Prime Numbers
for i in range(1,100):
    if i == 2:
        print(i)
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:
            print(i)
###############################################
#5 Know Basic Python Data Types and when to use them

string, list, tuples, dictionary, sets

#Lists
my_list = [10, 20, 30, 40]
for i in my_list:
    print(i)

#Tuples
my_tup = (1, 2, 3, 4, 5, 6, 7, 8 ,9, 10)
for i in my_tup:
    print(i)

#Dict
my_dict = {'name' : 'Bronx', 'age': '2', 'occupation' : "Corey's Dog"}
for key,val in my_dict.items():
    print("My {} is {}".format(key,val))

#Set ,No Dups
my_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
for i in my_set:
    print(i)
###############################################
#6 Know how to use List Comprehensions

my_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Give me each number in a list squared
squares = [ num**2 for num in my_list ]
print(squares)

###############################################
7. Know how to use generators

#Fibonacci Generator
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a+b

# num = fib(10)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))


for item in fib(10):
    print(item)

###############################################
8. Know the basics of OOP

class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My Name is {}".format(self.name))

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("...And I am {}".format(self.hero_name))

corey = Person('Corey')
corey.reveal_identity()

wade = SuperHero('Wade Wilson', 'DeadPool')
wade.reveal_identity()

###############################################
9. Have Python Related Questions ready to ask your interviewer

###############################################
10. Know Basics of other technologies




