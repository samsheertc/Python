'''
The below example is similar to a MAP function and it passes an arugment as a function.
Here the function takes a function and an array as its arguments and run each value of that array through 
the provided function and returns a new array of those results
'''

#Function is Passed as a parameter
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])

print(squares) #[1, 4, 9, 16, 25]
print(cubes)   #[1, 8, 27, 64, 125]

