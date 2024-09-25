
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name'])                 #John
print(student['courses'])              #['Math', 'CompSci']
print(student.get('name'))             #John
print(student.get('phone','NotFound')) #NotFound

#Add
student['phone'] = '2107495065'
print(student)
#{'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '2107495065'}

#Update
student['name'] = 'Jane'
print(student)  
#{'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '2107495065'}

#Update multiple field
student.update({'name': 'Joe', 'age': 30, 'courses': ['Phy', 'Che']})
print(student) #{'name': 'Joe', 'age': 30, 'courses': ['Phy', 'Che']}

#delete
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
del student['age']
print(student)     #{'name': 'John', 'courses': ['Math', 'CompSci']}

#pop method
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
age=student.pop('age')
print(age)      #25
print(student)  #{'name': 'John', 'courses': ['Math', 'CompSci']}


#Keys and Values
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(len(student))      #3
print(student.keys())    #dict_keys(['name', 'age', 'courses'])
print(student.values())  #dict_values(['John', 25, ['Math', 'CompSci']])
print(student.items())  #dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])


#Looping
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
