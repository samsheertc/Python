def square(x):
    return x * x

f = square
print(f)      #<function square at 0x000001AACB7F7010>
print(square) #<function square at 0x000001AACB7F7010>
print(f(5))   #25

#Here the variable hold the name of the function and can call the function using the variable name
