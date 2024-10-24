#-------------------------------------------------
#Unpacking
#Normal
items = (1, 2)
print(items)

#Unpacking
a, b = (1, 2)
print(a)
print(b)

a, _ = (1, 2)
print(a)
#print(b)

#Error
ValueError: too many values to unpack (expected 2)
a, b = (1, 2, 3)
print(a)
print(b)
#-------------------------------------------------
#Unpacking
#ValueError: too many values to unpack (expected 3)
a, b, c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)

a, b, *c, d = (1, 2, 3, 4, 5, 6,7)
print(a)
print(b)
print(c)
print(d)

a, b, *_, d = (1, 2, 3, 4, 5, 6,7)
print(a)
print(b)
#print(c)
print(d)
#-------------------------------------------------
