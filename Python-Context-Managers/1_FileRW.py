#Two way to use files

#regular method
f = open('sample.txt', 'w')
f.write('This text is written to file')
f.close()

#Using Context Manager
with open('sample.txt', 'w') as f:
    f.write('This again written to the file')