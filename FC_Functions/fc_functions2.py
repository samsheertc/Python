'''
A Function accepts other functions as arugments or return functions as their result is called as Higher - Order Function
This example is similar to a MAP function.
Here the function takes a function and an array as its arguments and run each value of that array through 
the provided function and returns a new array of those results
'''

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
