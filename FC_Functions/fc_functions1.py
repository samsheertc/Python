def square(x):
    return x * x

f = square
print(f)      #<function square at 0x000001AACB7F7010>
print(square) #<function square at 0x000001AACB7F7010>
print(f(5))   #25
